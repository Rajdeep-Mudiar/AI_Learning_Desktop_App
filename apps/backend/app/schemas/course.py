from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class LessonSummary(BaseModel):
    id: str
    slug: str
    title: str
    order: int
    estimated_minutes: int
    difficulty: str
    is_completed: bool = False

class ModuleDetail(BaseModel):
    id: str
    title: str
    description: str
    order: int
    lessons: List[LessonSummary]
    is_completed: bool = False
    completed_count: int = 0
    total_count: int = 0

class CourseSummary(BaseModel):
    id: str
    title: str
    slug: str
    description: str
    category: str
    level: str  # Beginner, Intermediate, Advanced
    estimated_hours: int
    icon: str
    color: str
    prerequisites: List[str] = []
    skills_taught: List[str] = []
    total_lessons: int = 0
    completed_lessons: int = 0
    progress_percentage: float = 0.0
    order: int = 1

class CourseDetail(CourseSummary):
    syllabus_overview: str
    modules: List[ModuleDetail]
    next_up_lesson_slug: Optional[str] = None
