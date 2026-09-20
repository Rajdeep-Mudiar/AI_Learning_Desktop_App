from typing import List, Dict, Any, Optional
from pydantic import BaseModel

class TestCaseResult(BaseModel):
    test_id: str
    description: str
    passed: bool
    expected_output: Optional[str] = None
    actual_output: Optional[str] = None
    error_message: Optional[str] = None
    is_hidden: bool = False

class ChallengeSummary(BaseModel):
    id: str
    title: str
    domain: str = "ai-ml"
    category: str
    difficulty: str  # Beginner, Intermediate, Advanced
    description: str
    skills_tested: List[str]
    xp_reward: int = 100
    is_completed: bool = False

class ChallengeDetail(ChallengeSummary):
    problem_statement: str
    starter_code: str
    hints: List[str]
    visible_test_cases_count: int
    total_test_cases_count: int

class ChallengeSubmissionRequest(BaseModel):
    challenge_id: str
    code: str

class ChallengeSubmissionResponse(BaseModel):
    challenge_id: str
    all_passed: bool
    passed_count: int
    total_count: int
    test_results: List[TestCaseResult]
    execution_duration_ms: float
    xp_earned: int
    feedback_message: str
    skill_updates: Dict[str, float] = {}
