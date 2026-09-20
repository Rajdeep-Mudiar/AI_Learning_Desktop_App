from typing import List, Dict, Any, Optional
from pydantic import BaseModel

class DiagnosticScenarioSummary(BaseModel):
    id: str
    title: str
    category: str
    difficulty: str
    description: str
    symptoms: List[str]
    xp_reward: int = 50

class DiagnosticScenarioDetail(DiagnosticScenarioSummary):
    code_snippet: str
    metrics_log: Dict[str, Any]
    hints: List[str]
    options: List[str]

class DiagnosticSubmissionRequest(BaseModel):
    scenario_id: str
    selected_option: int
    user_diagnosis: Optional[str] = None

class DiagnosticSubmissionResponse(BaseModel):
    scenario_id: str
    is_correct: bool
    explanation: str
    fix_code_snippet: str
    points_earned: int
    concept_mastered: str
