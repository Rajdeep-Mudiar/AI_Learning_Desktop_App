from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class EquationAnnotation(BaseModel):
    equation_latex: str
    equation_name: str
    plain_english_meaning: str
    geometric_intuition: str
    dimension_notes: str

class ReproductionStep(BaseModel):
    step_number: int
    title: str
    description: str
    hyperparameters: Dict[str, Any] = Field(default_factory=dict)
    executable_code: str
    expected_outcome: str
    is_completed: bool = False

class ResearchPaper(BaseModel):
    id: str
    title: str
    authors: List[str]
    year: int
    conference: str
    arxiv_id: str
    category: str  # "Transformers", "Vision", "Fine-Tuning", "Generative AI"
    abstract: str
    key_innovations: List[str]
    equations: List[EquationAnnotation]
    reproduction_steps: List[ReproductionStep]
    citation_count: int
    difficulty: str  # "Intermediate", "Advanced"

class PaperListItem(BaseModel):
    id: str
    title: str
    authors: List[str]
    year: int
    conference: str
    arxiv_id: str
    category: str
    abstract: str
    difficulty: str
    reproduction_steps_count: int

class ReproductionRunRequest(BaseModel):
    paper_id: str
    step_number: int
    custom_code: Optional[str] = None
