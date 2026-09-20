from typing import List
from app.schemas.achievement import AchievementBadge, UserAchievementsSummary

ALL_BADGES: List[AchievementBadge] = [
    # Curriculum
    AchievementBadge(
        id="b-math-foundations",
        title="Mathematical Foundations Master",
        description="Completed all Linear Algebra, Vector Calculus, and Probability quizzes with > 90% score.",
        icon="📐",
        category="Curriculum",
        tier="Gold",
        xp_reward=150,
        unlocked_at="2026-09-19T14:30:00Z",
        is_unlocked=True
    ),
    AchievementBadge(
        id="b-gradient-navigator",
        title="Gradient Navigator",
        description="Successfully traced forward and backpropagation gradient flow in the Neural Network Lab.",
        icon="⚡",
        category="Curriculum",
        tier="Silver",
        xp_reward=100,
        unlocked_at="2026-09-20T08:15:00Z",
        is_unlocked=True
    ),
    AchievementBadge(
        id="b-attention-architect",
        title="Attention Architect",
        description="Explored Scaled Dot-Product Attention matrices and Multi-Head token distributions.",
        icon="✨",
        category="Curriculum",
        tier="Diamond",
        xp_reward=200,
        unlocked_at="2026-09-20T10:10:00Z",
        is_unlocked=True
    ),

    # Coding & Sandbox
    AchievementBadge(
        id="b-numpy-vectorizer",
        title="NumPy Vectorization Wizard",
        description="Solved 3 autograded coding challenges from scratch using pure NumPy matrix math.",
        icon="💻",
        category="Coding",
        tier="Gold",
        xp_reward=150,
        unlocked_at="2026-09-20T05:00:00Z",
        is_unlocked=True
    ),
    AchievementBadge(
        id="b-sandbox-explorer",
        title="Sandbox Pioneer",
        description="Executed your first custom Python script in the isolated subprocess execution sandbox.",
        icon="🧪",
        category="Coding",
        tier="Bronze",
        xp_reward=50,
        unlocked_at="2026-09-19T18:20:00Z",
        is_unlocked=True
    ),
    AchievementBadge(
        id="b-diagnostic-surgeon",
        title="Model Diagnostic Surgeon",
        description="Diagnosed and resolved all 3 'Break the Model' failure scenarios without spoiling hints.",
        icon="🛠️",
        category="Coding",
        tier="Diamond",
        xp_reward=250,
        unlocked_at="2026-09-20T04:40:00Z",
        is_unlocked=True
    ),

    # Experimentation
    AchievementBadge(
        id="b-model-tuner-pro",
        title="Model Benchmark Specialist",
        description="Trained and compared 5+ classical ML models in the Experimentation Laboratory.",
        icon="📊",
        category="Experimentation",
        tier="Silver",
        xp_reward=100,
        unlocked_at="2026-09-20T09:12:00Z",
        is_unlocked=True
    ),
    AchievementBadge(
        id="b-roc-hunter",
        title="ROC & AUC Master",
        description="Achieved an Area Under the Curve (AUC) > 0.98 on a benchmark classification dataset.",
        icon="🎯",
        category="Experimentation",
        tier="Gold",
        xp_reward=150,
        unlocked_at="2026-09-20T09:45:00Z",
        is_unlocked=True
    ),

    # Projects & Viva
    AchievementBadge(
        id="b-viva-distinction",
        title="Viva Defense High Distinction",
        description="Defended your spam classification architecture in the AI Viva Oral Exam with Distinction.",
        icon="🏆",
        category="Projects",
        tier="Diamond",
        xp_reward=300,
        unlocked_at="2026-09-20T10:45:00Z",
        is_unlocked=True
    ),
    AchievementBadge(
        id="b-portfolio-ready",
        title="Portfolio Ready Engineer",
        description="Exported a production-ready GitHub README and resume summary for an end-to-end AI project.",
        icon="🚀",
        category="Projects",
        tier="Silver",
        xp_reward=100,
        unlocked_at=None,
        progress_percentage=80,
        is_unlocked=False
    )
]

def get_user_achievements() -> UserAchievementsSummary:
    unlocked = [b for b in ALL_BADGES if b.is_unlocked]
    total_xp = sum(b.xp_reward for b in unlocked)
    current_level = 1 + (total_xp // 250)
    next_level_xp = current_level * 250

    titles = [
        "AI Novice", "Gradient Explorer", "NumPy Practitioner",
        "ML Engineer Apprentice", "Neural Network Specialist",
        "AI Research Fellow", "Senior AI Systems Architect"
    ]
    level_title = titles[min(current_level - 1, len(titles) - 1)]

    return UserAchievementsSummary(
        total_xp=total_xp,
        current_level=current_level,
        next_level_xp=next_level_xp,
        level_title=level_title,
        total_badges_count=len(ALL_BADGES),
        unlocked_badges_count=len(unlocked),
        streak_days=7,
        badges=ALL_BADGES,
        certificate_eligible=len(unlocked) >= 6
    )
