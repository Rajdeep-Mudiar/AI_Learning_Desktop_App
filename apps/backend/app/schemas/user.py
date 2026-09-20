from datetime import datetime
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, EmailStr, Field

class LearningPreferences(BaseModel):
    theme: str = "dark"
    daily_goal_mins: int = 30
    preferred_track: str = "ai_engineer"
    notifications_enabled: bool = True

class StreakInfo(BaseModel):
    current: int = 1
    longest: int = 1
    last_active_date: Optional[str] = None
    completed_challenges_count: int = 0

class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    role: str = "student"

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=100)
    preferred_track: Optional[str] = "ai_engineer"

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserProfileUpdate(BaseModel):
    name: Optional[str] = None
    avatar_url: Optional[str] = None
    learning_preferences: Optional[LearningPreferences] = None

class UserOut(UserBase):
    id: str
    avatar_url: Optional[str] = None
    skill_mastery: Dict[str, float] = {}
    streak: StreakInfo = StreakInfo()
    learning_preferences: LearningPreferences = LearningPreferences()
    created_at: datetime
    updated_at: datetime

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut
