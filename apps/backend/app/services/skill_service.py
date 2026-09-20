from typing import List, Dict, Any
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.repositories.skill_repository import SkillRepository
from app.repositories.user_repository import UserRepository
from app.schemas.skill import SkillTreeResponse, SkillTreeCategory, SkillNode

class SkillService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.skill_repo = SkillRepository(db)
        self.user_repo = UserRepository(db)

    async def get_skill_tree(self, user_id: str) -> SkillTreeResponse:
        skills = await self.skill_repo.get_all()
        user = await self.user_repo.get_by_id(user_id)
        user_mastery = user.get("skill_mastery", {}) if user else {}
        
        categories_dict: Dict[str, List[SkillNode]] = {}
        category_totals: Dict[str, List[float]] = {}
        
        for s in skills:
            cat = s.get("category", "General AI")
            s_id = s["id"]
            mastery_pct = float(user_mastery.get(s_id, 0.0))
            
            node = SkillNode(
                id=s_id,
                category=cat,
                title=s["title"],
                description=s["description"],
                level=s.get("level", 0),
                prerequisites=s.get("prerequisites", []),
                icon=s.get("icon"),
                mastery_percentage=mastery_pct
            )
            categories_dict.setdefault(cat, []).append(node)
            category_totals.setdefault(cat, []).append(mastery_pct)
            
        categories_out = []
        radar_data = {}
        all_masteries = []
        
        for cat_name, node_list in categories_dict.items():
            scores = category_totals.get(cat_name, [0.0])
            avg_score = round(sum(scores) / max(1, len(scores)), 1)
            categories_out.append(SkillTreeCategory(
                category=cat_name,
                description=f"Core competencies in {cat_name}",
                skills=node_list,
                overall_mastery=avg_score
            ))
            radar_data[cat_name] = avg_score
            all_masteries.extend(scores)
            
        overall = round(sum(all_masteries) / max(1, len(all_masteries)), 1) if all_masteries else 0.0
        
        return SkillTreeResponse(
            categories=categories_out,
            overall_mastery=overall,
            radar_data=radar_data
        )
