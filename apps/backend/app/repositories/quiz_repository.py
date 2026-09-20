from typing import List, Optional, Dict, Any
from motor.motor_asyncio import AsyncIOMotorDatabase

class QuizRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db.quizzes

    async def get_by_id(self, quiz_id: str) -> Optional[dict]:
        return await self.collection.find_one({"id": quiz_id})

    async def get_by_lesson_slug(self, lesson_slug: str) -> Optional[dict]:
        return await self.collection.find_one({"lesson_slug": lesson_slug})

    async def create_or_update(self, quiz_doc: dict) -> dict:
        await self.collection.update_one(
            {"id": quiz_doc["id"]},
            {"$set": quiz_doc},
            upsert=True
        )
        return await self.get_by_id(quiz_doc["id"])
