from typing import List, Optional, Dict
from pydantic import BaseModel

class SkillNode(BaseModel):
    id: str
    category: str
    title: str
    description: str
    level: int = 0  # 0 to 4
    prerequisites: List[str] = []
    icon: Optional[str] = None
    mastery_percentage: float = 0.0

class SkillTreeCategory(BaseModel):
    category: str
    description: str
    skills: List[SkillNode]
    overall_mastery: float = 0.0

class SkillTreeResponse(BaseModel):
    categories: List[SkillTreeCategory]
    overall_mastery: float = 0.0
    radar_data: Dict[str, float] = {}
