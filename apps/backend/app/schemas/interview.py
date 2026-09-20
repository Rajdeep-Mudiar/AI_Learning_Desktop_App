from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class InterviewQuestion(BaseModel):
    id: str
    category: str  # "ML Theory", "System Design", "Coding & Vectorization", "Math & Calculus"
    question: str
    rubric: str
    expected_key_points: List[str]

class InterviewTrack(BaseModel):
    id: str
    title: str
    role_target: str
    difficulty: str  # "Junior", "Mid-Level", "Senior / Staff"
    duration_minutes: int
    questions_count: int
    description: str
    banner_color: str
    questions: List[InterviewQuestion]

class InterviewAnswerRequest(BaseModel):
    track_id: str
    question_id: str
    question: str
    user_answer: str

class QuestionFeedback(BaseModel):
    question_id: str
    score: int
    feedback: str
    strengths: List[str]
    missing_points: List[str]

class InterviewReport(BaseModel):
    overall_score: int
    recommendation: str  # "Strong Hire", "Hire", "Lean Hire", "No Hire"
    technical_depth_score: int
    communication_score: int
    problem_solving_score: int
    detailed_feedback: List[QuestionFeedback]
    strengths_summary: List[str]
    improvement_areas: List[str]

# Hackathon Schemas
class HackathonSubmissionRequest(BaseModel):
    challenge_id: str
    code: str
    model_name: Optional[str] = "Custom Estimator"

class LeaderboardEntry(BaseModel):
    rank: int
    username: str
    score: float
    latency_ms: float
    model_name: str
    submitted_at: str

class HackathonChallenge(BaseModel):
    id: str
    title: str
    tagline: str
    time_limit_minutes: int
    metric_name: str  # "F1-Score", "ROC-AUC", "Inference Speed (FPS)"
    target_benchmark: float
    description: str
    dataset_info: str
    starter_code: str
    leaderboard: List[LeaderboardEntry]
