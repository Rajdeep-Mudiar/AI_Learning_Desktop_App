from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class ProjectMilestone(BaseModel):
    id: str
    step_number: int
    title: str
    description: str
    tasks: List[str]
    starter_code: Optional[str] = None
    solution_code: Optional[str] = None
    is_completed: bool = False

class ProjectTrack(BaseModel):
    id: str
    title: str
    tagline: str
    difficulty: str  # "Beginner", "Intermediate", "Advanced"
    estimated_hours: int
    category: str  # "NLP", "Computer Vision", "Classical ML", "RAG & LLM"
    description: str
    dataset_name: str
    architecture: str
    skills_covered: List[str]
    milestones: List[ProjectMilestone]
    banner_gradient: str

class VivaQuestionRequest(BaseModel):
    project_id: str
    current_step: int = 1
    previous_answers: List[Dict[str, str]] = Field(default_factory=list)

class VivaQuestionResponse(BaseModel):
    question_id: str
    question: str
    focus_area: str  # "Architecture", "Math/Optimization", "Error Analysis", "Production/Deployment"
    rubric: str

class VivaSubmitAnswerRequest(BaseModel):
    project_id: str
    question_id: str
    question: str
    answer: str

class VivaEvaluationResponse(BaseModel):
    score: int  # 0 to 100
    grade: str  # "Distinction", "Merit", "Pass", "Needs Revision"
    strengths: List[str]
    areas_for_improvement: List[str]
    examiner_feedback: str

class PortfolioExportResponse(BaseModel):
    project_id: str
    markdown_readme: str
    resume_bullet_points: List[str]
    architecture_mermaid: str
