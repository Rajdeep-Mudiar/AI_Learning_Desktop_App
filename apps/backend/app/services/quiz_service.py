from typing import List, Dict, Any, Optional
from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.repositories.quiz_repository import QuizRepository
from app.repositories.lesson_repository import LessonRepository
from app.repositories.progress_repository import ProgressRepository
from app.repositories.user_repository import UserRepository
from app.schemas.quiz import (
    QuizDetail, QuizQuestionOut, QuizSubmissionRequest, 
    QuizSubmissionResponse, QuestionGradedResult
)

class QuizService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.quiz_repo = QuizRepository(db)
        self.lesson_repo = LessonRepository(db)
        self.progress_repo = ProgressRepository(db)
        self.user_repo = UserRepository(db)

    async def get_quiz_for_student(self, quiz_id: str) -> QuizDetail:
        quiz = await self.quiz_repo.get_by_id(quiz_id)
        if not quiz:
            # Fallback by lesson slug
            quiz = await self.quiz_repo.get_by_lesson_slug(quiz_id)
            
        if not quiz:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Quiz '{quiz_id}' was not found."
            )
            
        # Strip out the correct answers from questions for students
        sanitized_questions = []
        for q in quiz.get("questions", []):
            sanitized_questions.append(QuizQuestionOut(
                id=q["id"],
                type=q.get("type", "multiple_choice"),
                question=q["question"],
                options=q.get("options"),
                skill_tag=q.get("skill_tag", "general"),
                points=q.get("points", 10),
                hint=q.get("hint")
            ))
            
        return QuizDetail(
            id=quiz["id"],
            lesson_slug=quiz["lesson_slug"],
            title=quiz["title"],
            passing_score=quiz.get("passing_score", 70),
            questions=sanitized_questions
        )

    async def grade_submission(self, quiz_id: str, submission: QuizSubmissionRequest, user_id: str) -> QuizSubmissionResponse:
        quiz = await self.quiz_repo.get_by_id(quiz_id)
        if not quiz:
            quiz = await self.quiz_repo.get_by_lesson_slug(quiz_id)
            
        if not quiz:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Quiz '{quiz_id}' was not found."
            )
            
        questions_map = {q["id"]: q for q in quiz.get("questions", [])}
        user_answers_map = {a.question_id: a.selected_answer for a in submission.answers}
        
        results: List[QuestionGradedResult] = []
        total_earned = 0
        total_possible = 0
        skill_deltas: Dict[str, float] = {}
        
        for q_id, q_data in questions_map.items():
            max_pts = q_data.get("points", 10)
            total_possible += max_pts
            correct_ans = q_data.get("correct_answer")
            user_ans = user_answers_map.get(q_id)
            skill_tag = q_data.get("skill_tag", "general")
            
            is_correct = False
            q_type = q_data.get("type", "multiple_choice")
            
            if q_type == "multiple_choice" or q_type == "true_false":
                is_correct = (user_ans == correct_ans)
            elif q_type == "multiple_select":
                # Compare sets
                user_set = set(user_ans) if isinstance(user_ans, list) else set()
                correct_set = set(correct_ans) if isinstance(correct_ans, list) else set([correct_ans])
                is_correct = (user_set == correct_set)
            elif q_type == "fill_blank":
                if isinstance(user_ans, str) and isinstance(correct_ans, str):
                    is_correct = (user_ans.strip().lower() == correct_ans.strip().lower())
                elif isinstance(correct_ans, list):
                    is_correct = any(str(user_ans).strip().lower() == str(c).strip().lower() for c in correct_ans)
            else:
                is_correct = (user_ans == correct_ans)
                
            pts_earned = max_pts if is_correct else 0
            total_earned += pts_earned
            
            # Skill delta calculation
            delta = 6.0 if is_correct else -1.5
            skill_deltas[skill_tag] = skill_deltas.get(skill_tag, 0.0) + delta
            
            results.append(QuestionGradedResult(
                question_id=q_id,
                is_correct=is_correct,
                user_answer=user_ans,
                correct_answer=correct_ans,
                explanation=q_data.get("explanation", "Review the theoretical concept and mathematical formulation."),
                skill_tag=skill_tag,
                points_earned=pts_earned,
                max_points=max_pts,
                remedial_tip=q_data.get("remedial_tip") if not is_correct else None
            ))
            
        percentage = round((total_earned / max(1, total_possible)) * 100.0, 1)
        passed = percentage >= quiz.get("passing_score", 70)
        
        # Update user's skills
        updated_skills = {}
        for s_tag, delta in skill_deltas.items():
            updated_skills = await self.user_repo.update_skill_mastery(user_id, s_tag, delta)
            
        # Record progress
        lesson = await self.lesson_repo.get_by_slug(quiz["lesson_slug"])
        course_slug = lesson["course_slug"] if lesson else "ai_foundations"
        
        await self.progress_repo.record_quiz_result(
            user_id=user_id,
            course_slug=course_slug,
            quiz_id=quiz["id"],
            score=total_earned,
            max_score=total_possible,
            passed=passed
        )
        
        summary_msg = (
            f"Outstanding! You scored {percentage}% and demonstrated solid mastery."
            if passed else
            f"You scored {percentage}%. Review the detailed explanations below and try again to master this topic!"
        )
        
        return QuizSubmissionResponse(
            quiz_id=quiz["id"],
            lesson_slug=quiz["lesson_slug"],
            total_score=total_earned,
            max_score=total_possible,
            percentage=percentage,
            passed=passed,
            results=results,
            skill_mastery_updates=updated_skills,
            summary_message=summary_msg
        )
