from datetime import datetime, timezone
from typing import List, Dict, Any, Optional
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.repositories.user_repository import UserRepository
from app.repositories.course_repository import CourseRepository
from app.repositories.progress_repository import ProgressRepository
from app.repositories.lesson_repository import LessonRepository
from app.schemas.dashboard import (
    DashboardSummaryResponse, ContinueLearningWidget, SkillMasteryItem, 
    DailyChallengeWidget, RecommendedLesson, RecentExperimentPlaceholder, 
    ProjectProgressPlaceholder
)
from app.schemas.user import UserOut, StreakInfo, LearningPreferences

def get_level_label(pct: float) -> str:
    if pct < 20:
        return "Beginner"
    elif pct < 45:
        return "Familiar"
    elif pct < 70:
        return "Developing"
    elif pct < 90:
        return "Proficient"
    else:
        return "Mastery"

class DashboardService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.user_repo = UserRepository(db)
        self.course_repo = CourseRepository(db)
        self.progress_repo = ProgressRepository(db)
        self.lesson_repo = LessonRepository(db)

    async def get_dashboard_summary(self, user_id: str) -> DashboardSummaryResponse:
        user_doc = await self.user_repo.get_by_id(user_id)
        if not user_doc:
            user_doc = {
                "_id": user_id,
                "name": "Learner",
                "email": "student@ailearnlab.io",
                "role": "student",
                "avatar_url": None,
                "skill_mastery": {},
                "streak": {"current": 1, "longest": 1, "last_active_date": ""},
                "learning_preferences": {"theme": "dark", "daily_goal_mins": 30, "preferred_track": "ai_engineer"},
                "created_at": datetime.now(timezone.utc),
                "updated_at": datetime.now(timezone.utc)
            }
            
        user_out = UserOut(
            id=str(user_doc.get("_id", user_id)),
            name=user_doc.get("name", "Learner"),
            email=user_doc.get("email", ""),
            role=user_doc.get("role", "student"),
            avatar_url=user_doc.get("avatar_url"),
            skill_mastery=user_doc.get("skill_mastery", {}),
            streak=StreakInfo(**user_doc.get("streak", {})),
            learning_preferences=LearningPreferences(**user_doc.get("learning_preferences", {})),
            created_at=user_doc.get("created_at", datetime.now(timezone.utc)),
            updated_at=user_doc.get("updated_at", datetime.now(timezone.utc))
        )
        
        # Determine Greeting based on hour
        current_hour = datetime.now().hour
        if current_hour < 12:
            greeting_time = "Good morning"
        elif current_hour < 18:
            greeting_time = "Good afternoon"
        else:
            greeting_time = "Good evening"
            
        greeting = f"{greeting_time}, {user_out.name.split()[0]}! Continue your AI journey."
        
        # Continue Learning Widget
        progress_list = await self.progress_repo.get_all_user_progress(user_id)
        continue_widget = None
        total_completed_lessons = 0
        total_quizzes_passed = 0
        
        for p in progress_list:
            total_completed_lessons += len(p.get("completed_lessons", []))
            for q_id, q_res in p.get("quiz_scores", {}).items():
                if q_res.get("passed"):
                    total_quizzes_passed += 1
                    
        # Find the most recently active or first uncompleted course
        active_progress = None
        for p in sorted(progress_list, key=lambda x: x.get("updated_at", datetime.min), reverse=True):
            if p.get("percentage", 0) < 100:
                active_progress = p
                break
                
        courses = await self.course_repo.get_all()
        if courses:
            target_course = courses[0]
            if active_progress:
                found = next((c for c in courses if c["slug"] == active_progress["course_slug"]), None)
                if found:
                    target_course = found
                    
            lessons = await self.course_repo.get_course_lessons(target_course["slug"])
            completed_set = set(active_progress.get("completed_lessons", []) if active_progress else [])
            
            # Find next lesson
            target_lesson = None
            for l in lessons:
                if l["slug"] not in completed_set:
                    target_lesson = l
                    break
            if not target_lesson and lessons:
                target_lesson = lessons[0]
                
            if target_lesson:
                # Find module title
                module_title = "Core Foundations"
                for m in target_course.get("modules", []):
                    if m["id"] == target_lesson.get("module_id"):
                        module_title = m["title"]
                        break
                        
                continue_widget = ContinueLearningWidget(
                    course_slug=target_course["slug"],
                    course_title=target_course["title"],
                    course_color=target_course.get("color", "#4F46E5"),
                    course_icon=target_course.get("icon", "Code"),
                    lesson_slug=target_lesson["slug"],
                    lesson_title=target_lesson["title"],
                    estimated_minutes=target_lesson.get("estimated_minutes", 15),
                    course_percentage=active_progress.get("percentage", 0.0) if active_progress else 0.0,
                    module_title=module_title
                )
                
        # Skill mastery bars for top 5 key areas
        skill_dict = user_doc.get("skill_mastery", {})
        key_skills = [
            ("python_basics", "Python Programming", "Programming"),
            ("linear_algebra", "Math for ML (Linear Algebra)", "Mathematics"),
            ("supervised_learning", "Classical Machine Learning", "Machine Learning"),
            ("neural_networks", "Deep Learning Foundations", "Deep Learning"),
            ("transformers", "Generative AI & LLMs", "Generative AI")
        ]
        
        skill_bars = []
        for s_id, s_name, s_cat in key_skills:
            val = float(skill_dict.get(s_id, 0.0))
            skill_bars.append(SkillMasteryItem(
                skill_id=s_id,
                name=s_name,
                percentage=val,
                category=s_cat,
                level_label=get_level_label(val)
            ))
            
        # Daily challenge
        today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        daily_challenge = DailyChallengeWidget(
            id=f"daily-{today_str}",
            date=today_str,
            title="Matrix Multiplication Dimension Rule",
            category="Mathematics for AI",
            difficulty="Easy",
            description="If matrix A is size (3, 4) and matrix B is size (4, 2), what is the shape of their dot product AB?",
            points=50,
            is_completed=False,
            options=["(3, 2)", "(4, 4)", "(3, 4)", "(2, 3)"],
            question_type="multiple_choice"
        )
        
        # Recommended lessons based on lowest mastery
        lowest_skill = min(skill_bars, key=lambda x: x.percentage) if skill_bars else None
        rec_lessons = [
            RecommendedLesson(
                course_slug="math-for-ai",
                lesson_slug="math-matrix-multiplication",
                course_title="Mathematics for AI",
                lesson_title="Matrix Multiplication & Geometric Transformations",
                reason=f"Recommended to boost your {lowest_skill.name if lowest_skill else 'Mathematics'} mastery.",
                difficulty="Intermediate",
                estimated_minutes=15
            ),
            RecommendedLesson(
                course_slug="ml-fundamentals",
                lesson_slug="ml-gradient-descent-intuition",
                course_title="Machine Learning Fundamentals",
                lesson_title="Gradient Descent Intuition & Loss Surface Navigation",
                reason="Core prerequisite for deep learning and neural network training.",
                difficulty="Beginner",
                estimated_minutes=20
            )
        ]
        
        # Placeholders for future phases (clearly identified)
        recent_exp = [
            RecentExperimentPlaceholder(
                id="EXP-001",
                title="Linear Regression Baseline",
                model_type="Scikit-Learn OLS",
                accuracy=0.92,
                status="Completed",
                timestamp="2 hours ago"
            ),
            RecentExperimentPlaceholder(
                id="EXP-002",
                title="KNN Distance Metric Comparison",
                model_type="K-Nearest Neighbors",
                accuracy=0.88,
                status="Completed",
                timestamp="Yesterday"
            )
        ]
        
        proj_progress = [
            ProjectProgressPlaceholder(
                id="PRJ-01",
                title="Spam Classifier from Scratch",
                domain="NLP & ML",
                status="In Progress",
                completion_percentage=45.0
            ),
            ProjectProgressPlaceholder(
                id="PRJ-02",
                title="Credit Risk Neural Predictor",
                domain="Deep Learning",
                status="Planning",
                completion_percentage=15.0
            )
        ]
        
        return DashboardSummaryResponse(
            user=user_out,
            greeting=greeting,
            continue_learning=continue_widget,
            skill_mastery_bars=skill_bars,
            daily_challenge=daily_challenge,
            recommended_learning=rec_lessons,
            streak_info=user_out.streak,
            recent_experiments=recent_exp,
            projects_in_progress=proj_progress,
            total_lessons_completed=total_completed_lessons,
            total_quizzes_passed=total_quizzes_passed
        )
