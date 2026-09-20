from typing import List, Optional, Dict, Any
from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.repositories.course_repository import CourseRepository
from app.repositories.progress_repository import ProgressRepository
from app.schemas.course import CourseSummary, CourseDetail, ModuleDetail, LessonSummary

class CourseService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.course_repo = CourseRepository(db)
        self.progress_repo = ProgressRepository(db)

    async def list_courses(self, user_id: Optional[str] = None) -> List[CourseSummary]:
        courses = await self.course_repo.get_all()
        user_progress_map = {}
        if user_id:
            progress_list = await self.progress_repo.get_all_user_progress(user_id)
            user_progress_map = {p["course_slug"]: p for p in progress_list}
            
        summaries = []
        for c in courses:
            lessons = await self.course_repo.get_course_lessons(c["slug"])
            total_lessons = len(lessons)
            
            p_data = user_progress_map.get(c["slug"], {})
            completed_count = len(p_data.get("completed_lessons", []))
            percentage = p_data.get("percentage", 0.0)
            
            summaries.append(CourseSummary(
                id=str(c.get("_id", c["slug"])),
                title=c["title"],
                slug=c["slug"],
                description=c["description"],
                domain=c.get("domain", "ai-ml"),
                category=c.get("category", "Artificial Intelligence"),
                level=c.get("level", "Beginner"),
                estimated_hours=c.get("estimated_hours", 10),
                icon=c.get("icon", "Code"),
                color=c.get("color", "#4F46E5"),
                prerequisites=c.get("prerequisites", []),
                skills_taught=c.get("skills_taught", []),
                total_lessons=total_lessons,
                completed_lessons=completed_count,
                progress_percentage=percentage,
                order=c.get("order", 1)
            ))
        return summaries

    async def get_course_detail(self, course_slug: str, user_id: Optional[str] = None) -> CourseDetail:
        course = await self.course_repo.get_by_slug(course_slug)
        if not course:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Course with slug '{course_slug}' not found."
            )
            
        lessons = await self.course_repo.get_course_lessons(course_slug)
        user_progress = None
        completed_set = set()
        if user_id:
            user_progress = await self.progress_repo.get_user_course_progress(user_id, course_slug)
            if user_progress:
                completed_set = set(user_progress.get("completed_lessons", []))
                
        # Group lessons into modules
        modules_data = course.get("modules", [])
        module_details = []
        
        # Build lookup of lessons by module_id
        lessons_by_module: Dict[str, List[dict]] = {}
        for l in lessons:
            mod_id = l.get("module_id", "default")
            lessons_by_module.setdefault(mod_id, []).append(l)
            
        next_up_lesson = None
        for m in modules_data:
            m_id = m["id"]
            m_lessons = lessons_by_module.get(m_id, [])
            m_lessons_sorted = sorted(m_lessons, key=lambda x: x.get("order", 1))
            
            lesson_summaries = []
            m_completed_count = 0
            for l in m_lessons_sorted:
                is_comp = l["slug"] in completed_set
                if is_comp:
                    m_completed_count += 1
                elif next_up_lesson is None:
                    next_up_lesson = l["slug"]
                    
                lesson_summaries.append(LessonSummary(
                    id=str(l.get("_id", l["slug"])),
                    slug=l["slug"],
                    title=l["title"],
                    order=l.get("order", 1),
                    estimated_minutes=l.get("estimated_minutes", 15),
                    difficulty=l.get("difficulty", "Beginner"),
                    is_completed=is_comp
                ))
                
            module_details.append(ModuleDetail(
                id=m_id,
                title=m["title"],
                description=m.get("description", ""),
                order=m.get("order", 1),
                lessons=lesson_summaries,
                is_completed=len(m_lessons_sorted) > 0 and m_completed_count == len(m_lessons_sorted),
                completed_count=m_completed_count,
                total_count=len(m_lessons_sorted)
            ))
            
        if not next_up_lesson and lessons:
            next_up_lesson = lessons[0]["slug"]
            
        total_lessons = len(lessons)
        completed_lessons = len(completed_set)
        percentage = round((completed_lessons / max(1, total_lessons)) * 100.0, 1) if total_lessons > 0 else 0.0
        
        return CourseDetail(
            id=str(course.get("_id", course["slug"])),
            title=course["title"],
            slug=course["slug"],
            description=course["description"],
            domain=course.get("domain", "ai-ml"),
            category=course.get("category", "Artificial Intelligence"),
            level=course.get("level", "Beginner"),
            estimated_hours=course.get("estimated_hours", 10),
            icon=course.get("icon", "Code"),
            color=course.get("color", "#4F46E5"),
            prerequisites=course.get("prerequisites", []),
            skills_taught=course.get("skills_taught", []),
            total_lessons=total_lessons,
            completed_lessons=completed_lessons,
            progress_percentage=percentage,
            order=course.get("order", 1),
            syllabus_overview=course.get("syllabus_overview", course["description"]),
            modules=module_details,
            next_up_lesson_slug=next_up_lesson
        )
