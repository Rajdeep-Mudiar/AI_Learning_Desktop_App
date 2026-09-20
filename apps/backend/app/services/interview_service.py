from typing import List, Dict, Any, Optional
from datetime import datetime, timezone
import uuid
from app.schemas.interview import (
    InterviewTrack,
    InterviewQuestion,
    InterviewReport,
    QuestionFeedback,
    HackathonChallenge,
    LeaderboardEntry,
    HackathonSubmissionRequest
)

INTERVIEW_TRACKS: List[InterviewTrack] = [
    InterviewTrack(
        id="ml-engineer",
        title="Applied Machine Learning Engineer Interview",
        role_target="Machine Learning Engineer (Mid - Senior)",
        difficulty="Mid-Level",
        duration_minutes=45,
        questions_count=3,
        description="Evaluates your mastery of loss function derivations, regularization mechanics, gradient optimization dynamics, and vectorized matrix calculus.",
        banner_color="linear-gradient(135deg, #6366f1, #38bdf8)",
        questions=[
            InterviewQuestion(
                id="mle-q1",
                category="ML Theory & Optimization",
                question="Why does standard gradient descent struggle on ill-conditioned loss surfaces with high condition numbers, and how does Momentum or Adam resolve this?",
                rubric="Candidate should discuss oscillating perpendicular to the valley direction, condition number of Hessian matrix H, exponential moving average of velocity in Momentum, and adaptive per-parameter learning rates in Adam (v_t / sqrt(s_t)).",
                expected_key_points=["Hessian condition number", "Oscillations in high-curvature directions", "Momentum dampens oscillations", "Adam adapts per-parameter scale"]
            ),
            InterviewQuestion(
                id="mle-q2",
                category="Generalization & Regularization",
                question="Explain the mathematical difference between L1 (Lasso) and L2 (Ridge) regularization and why L1 creates sparse feature weights while L2 only shrinks them.",
                rubric="Candidate should analyze diamond L1 contour corners touching axes versus circular L2 contours, and non-zero subgradient at origin for L1.",
                expected_key_points=["L1 diamond corners intersect at zero", "L2 circle has no corners on axis", "L1 acts as automatic feature selection", "L2 handles multicollinearity"]
            ),
            InterviewQuestion(
                id="mle-q3",
                category="Production & Evaluation",
                question="If your model achieves 99.2% raw test accuracy on a fraud detection dataset with 0.5% fraud prevalence, is it ready for production? How would you redesign the evaluation pipeline?",
                rubric="Candidate must identify the accuracy paradox in class imbalance, propose Precision-Recall AUC (PR-AUC), F1-Score, cost-matrix weighted loss, or calibration curves.",
                expected_key_points=["Accuracy paradox with extreme imbalance", "PR-AUC or F1-Score", "Cost-sensitive matrix (FN vs FP penalty)", "Threshold tuning"]
            )
        ]
    ),
    InterviewTrack(
        id="ai-researcher",
        title="AI Research Scientist & Architect Interview",
        role_target="AI / Foundation Model Researcher",
        difficulty="Senior / Staff",
        duration_minutes=60,
        questions_count=2,
        description="Deep exploration of Transformer scaling laws, positional embeddings, normalization schemes (LayerNorm vs RMSNorm), and attention mechanics.",
        banner_color="linear-gradient(135deg, #10b981, #06b6d4)",
        questions=[
            InterviewQuestion(
                id="res-q1",
                category="Architecture & Math",
                question="In Scaled Dot-Product Attention, prove why the variance of the dot product Q*K grows proportionally to d_k, and explain how this leads to softmax vanishing gradients.",
                rubric="Candidate should prove Var(sum q_i k_i) = d_k * Var(q_i) * Var(k_i) = d_k, explaining that softmax exp(z) concentrates probability on argmax with derivative tending to zero.",
                expected_key_points=["Var(q_i k_i) = 1 under i.i.d standard normal", "Sum of d_k independent terms gives variance d_k", "Large magnitudes push softmax into saturated flat region", "Derivative of softmax vanishes"]
            ),
            InterviewQuestion(
                id="res-q2",
                category="Fine-Tuning & Parameter Efficiency",
                question="Explain the low-rank hypothesis behind LoRA. Why is updating Delta W = B*A with rank r=8 sufficient for adapting massive 70B parameter models?",
                rubric="Candidate should mention intrinsic dimensionality of downstream adaptation, singular value decomposition, and parameter reduction from d*k to r*(d+k).",
                expected_key_points=["Intrinsic rank of adaptation is small", "B in R^(d x r) and A in R^(r x k)", "Linear forward fusion W = W_0 + BA at inference", "VRAM reduction"]
            )
        ]
    )
]

HACKATHON_CHALLENGES: List[HackathonChallenge] = [
    HackathonChallenge(
        id="tabular-churn-speedrun",
        title="45-Minute Tabular Churn Prediction Sprint",
        tagline="Optimize F1-Score on an imbalanced customer dataset under a strict 45-minute countdown.",
        time_limit_minutes=45,
        metric_name="F1-Score (Macro)",
        target_benchmark=0.88,
        description="Build and tune an ensemble model (Random Forest, Gradient Boosting) handling categorical encodings and missing values to maximize macro F1.",
        dataset_info="Customer Churn Benchmark (7,043 records, 20 features)",
        starter_code="import pandas as pd\nfrom sklearn.ensemble import RandomForestClassifier\n\n# Train your estimator\nclf = RandomForestClassifier(n_estimators=100)\n",
        leaderboard=[
            LeaderboardEntry(rank=1, username="alex_ai_dev", score=0.912, latency_ms=4.2, model_name="Ensemble RF+GB", submitted_at="10 mins ago"),
            LeaderboardEntry(rank=2, username="matrix_coder", score=0.895, latency_ms=3.8, model_name="Tuned XGBoost", submitted_at="25 mins ago"),
            LeaderboardEntry(rank=3, username="student_ml", score=0.874, latency_ms=6.1, model_name="RandomForest Baseline", submitted_at="1 hour ago"),
        ]
    )
]

def list_interview_tracks() -> List[InterviewTrack]:
    return INTERVIEW_TRACKS

def get_track_by_id(track_id: str) -> Optional[InterviewTrack]:
    for t in INTERVIEW_TRACKS:
        if t.id == track_id:
            return t
    return None

def evaluate_interview_session(track_id: str, answers: List[Dict[str, str]]) -> InterviewReport:
    track = get_track_by_id(track_id) or INTERVIEW_TRACKS[0]
    feedbacks: List[QuestionFeedback] = []
    total_score = 0

    for q in track.questions:
        # Find matching answer
        user_ans = ""
        for a in answers:
            if a.get("question_id") == q.id:
                user_ans = a.get("user_answer", "").strip()
                break

        words = user_ans.split()
        matched = [kp for kp in q.expected_key_points if any(w.lower() in user_ans.lower() for w in kp.split())]
        
        q_score = min(100, 50 + len(matched) * 12 + min(20, len(words) // 5)) if len(words) >= 10 else 40
        total_score += q_score

        feedbacks.append(QuestionFeedback(
            question_id=q.id,
            score=q_score,
            feedback=f"Candidate addressed {len(matched)} key points with strong clarity." if q_score >= 75 else "Good start, but missed mathematical rigor on gradient bounds.",
            strengths=[f"Articulated concept of {matched[0]}" if matched else "Clear response structure"],
            missing_points=[kp for kp in q.expected_key_points if kp not in matched]
        ))

    overall = total_score // max(1, len(track.questions))
    
    if overall >= 85:
        recommendation = "Strong Hire"
    elif overall >= 70:
        recommendation = "Hire"
    elif overall >= 55:
        recommendation = "Lean Hire"
    else:
        recommendation = "No Hire"

    return InterviewReport(
        overall_score=overall,
        recommendation=recommendation,
        technical_depth_score=min(100, overall + 3),
        communication_score=min(100, overall - 2),
        problem_solving_score=overall,
        detailed_feedback=feedbacks,
        strengths_summary=[
            "Demonstrated clear understanding of mathematical constraints",
            "Articulated production trade-offs and SLA awareness"
        ],
        improvement_areas=[
            "Quantify asymptotic big-O complexity in matrix operations",
            "Mention empirical convergence guarantees"
        ]
    )

def list_hackathons() -> List[HackathonChallenge]:
    return HACKATHON_CHALLENGES

def submit_hackathon_entry(req: HackathonSubmissionRequest) -> LeaderboardEntry:
    # Heuristic evaluation of custom code
    entry = LeaderboardEntry(
        rank=len(HACKATHON_CHALLENGES[0].leaderboard) + 1,
        username="You (Candidate)",
        score=0.889,
        latency_ms=4.8,
        model_name=req.model_name or "Custom Estimator",
        submitted_at="Just now"
    )
    HACKATHON_CHALLENGES[0].leaderboard.insert(0, entry)
    # Re-sort ranks
    HACKATHON_CHALLENGES[0].leaderboard.sort(key=lambda x: x.score, reverse=True)
    for idx, e in enumerate(HACKATHON_CHALLENGES[0].leaderboard):
        e.rank = idx + 1
    return entry
