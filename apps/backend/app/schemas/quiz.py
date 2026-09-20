from typing import List, Optional, Union, Any, Dict
from pydantic import BaseModel, Field

class QuizQuestionOut(BaseModel):
    id: str
    type: str  # multiple_choice, multiple_select, true_false, fill_blank
    question: str
    options: Optional[List[str]] = None
    skill_tag: str
    points: int = 10
    hint: Optional[str] = None

class QuizSubmissionItem(BaseModel):
    question_id: str
    selected_answer: Any  # int, list of ints, or string

class QuizSubmissionRequest(BaseModel):
    answers: List[QuizSubmissionItem]

class QuestionGradedResult(BaseModel):
    question_id: str
    is_correct: bool
    user_answer: Any
    correct_answer: Any
    explanation: str
    skill_tag: str
    points_earned: int
    max_points: int
    remedial_tip: Optional[str] = None

class QuizSubmissionResponse(BaseModel):
    quiz_id: str
    lesson_slug: str
    total_score: int
    max_score: int
    percentage: float
    passed: bool
    results: List[QuestionGradedResult]
    skill_mastery_updates: Dict[str, float]
    summary_message: str

class QuizDetail(BaseModel):
    id: str
    lesson_slug: str
    title: str
    passing_score: int = 70
    questions: List[QuizQuestionOut]
