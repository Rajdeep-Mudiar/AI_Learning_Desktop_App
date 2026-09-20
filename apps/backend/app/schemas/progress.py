from datetime import datetime
from typing import List, Dict, Any, Optional
from pydantic import BaseModel

class QuizAttemptRecord(BaseModel):
    score: int
    max_score: int
    percentage: float
    passed: bool
    attempts: int
    last_attempt_date: datetime

class CourseProgressOut(BaseModel):
    course_slug: str
    completed_lessons: List[str]
    percentage: float
    last_lesson_slug: Optional[str] = None
    quiz_scores: Dict[str, QuizAttemptRecord] = {}
    updated_at: datetime
