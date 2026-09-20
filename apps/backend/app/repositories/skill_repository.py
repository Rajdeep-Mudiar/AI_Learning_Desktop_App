from typing import List, Optional, Dict, Any
from motor.motor_asyncio import AsyncIOMotorDatabase

class SkillRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db.skills

    async def get_all(self) -> List[dict]:
        cursor = self.collection.find().sort("level", 1)
        return await cursor.to_list(length=100)

    async def create_or_update(self, skill_doc: dict) -> dict:
        await self.collection.update_one(
            {"id": skill_doc["id"]},
            {"$set": skill_doc},
            upsert=True
        )
        return skill_doc
