from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class AchievementBadge(BaseModel):
    id: str
    title: str
    description: str
    icon: str
    category: str  # "Curriculum", "Coding", "Experimentation", "Projects", "Community"
    tier: str  # "Bronze", "Silver", "Gold", "Diamond"
    xp_reward: int
    unlocked_at: Optional[str] = None
    progress_percentage: int = 100
    is_unlocked: bool = True

class UserAchievementsSummary(BaseModel):
    total_xp: int
    current_level: int
    next_level_xp: int
    level_title: str
    total_badges_count: int
    unlocked_badges_count: int
    streak_days: int
    badges: List[AchievementBadge]
    certificate_eligible: bool = False
