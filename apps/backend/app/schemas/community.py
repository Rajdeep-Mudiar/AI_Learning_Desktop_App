from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class PostComment(BaseModel):
    id: str
    author_name: str
    author_avatar: str
    content: str
    created_at: str
    upvotes: int = 0

class CommunityPost(BaseModel):
    id: str
    title: str
    author_name: str
    author_title: str
    author_avatar: str
    category: str  # "Show & Tell", "Algorithm Debugging", "Research Paper Club", "Interview Prep"
    content: str
    code_snippet: Optional[str] = None
    tags: List[str] = Field(default_factory=list)
    upvotes: int = 0
    comments_count: int = 0
    created_at: str
    comments: List[PostComment] = Field(default_factory=list)

class CreatePostRequest(BaseModel):
    title: str
    category: str
    content: str
    code_snippet: Optional[str] = None
    tags: List[str] = Field(default_factory=list)

# Career Roadmaps
class RoleSkillRequirement(BaseModel):
    skill_name: str
    importance: str  # "Must Have", "Important", "Good to Have"
    is_mastered: bool
    matching_course: str

class CareerPath(BaseModel):
    id: str
    role_title: str
    average_salary: str
    description: str
    market_demand: str  # "Very High", "High", "Growing"
    skills_required: List[RoleSkillRequirement]
    readiness_percentage: int

class CareerOverviewResponse(BaseModel):
    career_paths: List[CareerPath]
    recommended_focus_areas: List[str]
