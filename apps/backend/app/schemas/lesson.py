from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class TheorySection(BaseModel):
    title: str
    content_markdown: str
    key_takeaway: Optional[str] = None
    math_latex: Optional[str] = None

class VisualExplainer(BaseModel):
    type: str  # diagram, simulation_preview, chart, architecture_flow
    title: str
    subtitle: Optional[str] = None
    diagram_type: Optional[str] = None  # e.g., "linear_regression", "neural_net", "matrix_mult", "attention"
    parameters: Optional[Dict[str, Any]] = None
    data_points: Optional[List[Dict[str, Any]]] = None

class CodeExample(BaseModel):
    language: str = "python"
    title: str
    code: str
    explanation: str
    output_preview: Optional[str] = None

class LessonBase(BaseModel):
    title: str
    slug: str
    course_slug: str
    module_id: str
    order: int
    estimated_minutes: int
    difficulty: str
    learning_objectives: List[str]
    summary: str

class LessonDetail(LessonBase):
    id: str
    theory_sections: List[TheorySection]
    visual_explainer: Optional[VisualExplainer] = None
    code_example: Optional[CodeExample] = None
    quiz_id: Optional[str] = None
    next_lesson_slug: Optional[str] = None
    prev_lesson_slug: Optional[str] = None
    is_completed: bool = False

class LessonCompletionResponse(BaseModel):
    lesson_slug: str
    course_slug: str
    is_completed: bool
    course_percentage: float
    xp_earned: int
    updated_streak: int
    next_lesson_slug: Optional[str] = None
