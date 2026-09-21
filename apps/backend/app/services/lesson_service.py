from typing import Optional
from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.repositories.lesson_repository import LessonRepository
from app.repositories.course_repository import CourseRepository
from app.repositories.progress_repository import ProgressRepository
from app.repositories.user_repository import UserRepository
from app.schemas.lesson import LessonDetail, LessonCompletionResponse

class LessonService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.lesson_repo = LessonRepository(db)
        self.course_repo = CourseRepository(db)
        self.progress_repo = ProgressRepository(db)
        self.user_repo = UserRepository(db)

    async def get_lesson_by_slug(self, slug: str, user_id: Optional[str] = None) -> LessonDetail:
        lesson = await self.lesson_repo.get_by_slug(slug)
        if not lesson:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Lesson with slug '{slug}' was not found."
            )
            
        course_slug = lesson.get("course_slug")
        if not course_slug:
            # Look up course by course_id
            c_id = lesson.get("course_id")
            if c_id:
                course = await self.course_repo.get_by_slug(c_id)
                if not course:
                    course = await self.course_repo.collection.find_one({"id": c_id})
                if course:
                    course_slug = course.get("slug", c_id)
            if not course_slug:
                course_slug = "dsa-foundations-arrays-strings"
                
        is_completed = False
        if user_id:
            course_progress = await self.progress_repo.get_user_course_progress(user_id, course_slug)
            if course_progress:
                is_completed = slug in course_progress.get("completed_lessons", [])
                
        theory_sections = lesson.get("theory_sections", [])
        if not theory_sections and lesson.get("content"):
            raw_content = lesson.get("content", "")
            theory_sections = [{
                "title": f"Understanding {lesson.get('title', 'Core Concepts')}",
                "content_markdown": raw_content,
                "key_takeaway": f"Mastering {lesson.get('title', 'this topic')} provides essential foundational knowledge for modern engineering."
            }]
            
        learning_objectives = lesson.get("learning_objectives", [])
        if not learning_objectives:
            learning_objectives = [
                f"Understand the core architecture and principles of {lesson.get('title', 'this topic')}",
                "Analyze practical trade-offs and performance implications",
                "Apply best practices and design patterns in real-world scenarios"
            ]
            
        summary = lesson.get("summary", "")
        if not summary:
            summary = f"You completed {lesson.get('title', 'this lesson')}. You now have practical mastery over the underlying mechanics and trade-offs."
                
        # Determine domain from lesson or course
        domain = lesson.get("domain")
        if not domain and course_slug:
            if course_slug.startswith("web-") or course_slug.startswith("html") or course_slug.startswith("css") or course_slug.startswith("react") or course_slug.startswith("nodejs"):
                domain = "web-dev"
            elif course_slug.startswith("dsa-"):
                domain = "dsa"
            elif course_slug.startswith("cyber"):
                domain = "cybersecurity"
            elif course_slug.startswith("app-") or course_slug.startswith("flutter") or course_slug.startswith("mobile"):
                domain = "app-dev"
            elif course_slug.startswith("git-") or course_slug.startswith("github"):
                domain = "github"
            elif course_slug.startswith("sys-") or course_slug.startswith("system-"):
                domain = "system-design"
            else:
                domain = "ai-ml"
                
        return LessonDetail(
            id=str(lesson.get("_id", lesson["slug"])),
            title=lesson["title"],
            slug=lesson["slug"],
            course_slug=course_slug,
            domain=domain,
            module_id=lesson.get("module_id", "default"),
            order=lesson.get("order", 1),
            estimated_minutes=lesson.get("estimated_minutes", 15),
            difficulty=lesson.get("difficulty", "Beginner"),
            learning_objectives=learning_objectives,
            theory_sections=theory_sections,
            visual_explainer=lesson.get("visual_explainer"),
            code_example=lesson.get("code_example"),
            quiz_id=lesson.get("quiz_id"),
            summary=summary,
            next_lesson_slug=lesson.get("next_lesson_slug"),
            prev_lesson_slug=lesson.get("prev_lesson_slug"),
            is_completed=is_completed
        )

    async def complete_lesson(self, slug: str, user_id: str) -> LessonCompletionResponse:
        lesson = await self.lesson_repo.get_by_slug(slug)
        if not lesson:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Lesson with slug '{slug}' was not found."
            )
            
        course_slug = lesson["course_slug"]
        all_lessons = await self.course_repo.get_course_lessons(course_slug)
        total_lessons = len(all_lessons)
        
        progress_doc = await self.progress_repo.mark_lesson_completed(
            user_id=user_id,
            course_slug=course_slug,
            lesson_slug=slug,
            total_lessons=total_lessons
        )
        
        # Give skill mastery boost if associated with tags
        skill_tag = lesson.get("skill_tag", "python_basics")
        await self.user_repo.update_skill_mastery(user_id, skill_tag, 5.0)
        
        # Update streak
        streak = await self.user_repo.update_streak(user_id)
        
        return LessonCompletionResponse(
            lesson_slug=slug,
            course_slug=course_slug,
            is_completed=True,
            course_percentage=progress_doc.get("percentage", 0.0),
            xp_earned=25,
            updated_streak=streak.get("current", 1),
            next_lesson_slug=lesson.get("next_lesson_slug")
        )
