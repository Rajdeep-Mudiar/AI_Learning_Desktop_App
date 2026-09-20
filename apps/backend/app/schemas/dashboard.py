from typing import List, Optional, Dict, Any
from pydantic import BaseModel
from app.schemas.user import UserOut, StreakInfo
from app.schemas.course import CourseSummary

class DailyChallengeWidget(BaseModel):
    id: str
    date: str
    title: str
    category: str
    difficulty: str
    description: str
    points: int
    is_completed: bool = False
    options: Optional[List[str]] = None
    question_type: str = "multiple_choice"

class ContinueLearningWidget(BaseModel):
    course_slug: str
    course_title: str
    course_color: str
    course_icon: str
    lesson_slug: str
    lesson_title: str
    estimated_minutes: int
    course_percentage: float
    module_title: str

class SkillMasteryItem(BaseModel):
    skill_id: str
    name: str
    percentage: float
    category: str
    level_label: str  # Beginner, Developing, Proficient, Advanced, Mastery

class RecommendedLesson(BaseModel):
    course_slug: str
    course_title: str
    lesson_slug: str
    lesson_title: str
    reason: str
    difficulty: str
    estimated_minutes: int

class RecentExperimentPlaceholder(BaseModel):
    id: str
    title: str
    model_type: str
    accuracy: Optional[float] = None
    status: str
    timestamp: str

class ProjectProgressPlaceholder(BaseModel):
    id: str
    title: str
    domain: str
    status: str
    completion_percentage: float

class DashboardSummaryResponse(BaseModel):
    user: UserOut
    greeting: str
    continue_learning: Optional[ContinueLearningWidget] = None
    skill_mastery_bars: List[SkillMasteryItem]
    daily_challenge: DailyChallengeWidget
    recommended_learning: List[RecommendedLesson]
    streak_info: StreakInfo
    recent_experiments: List[RecentExperimentPlaceholder]
    projects_in_progress: List[ProjectProgressPlaceholder]
    total_lessons_completed: int
    total_quizzes_passed: int
