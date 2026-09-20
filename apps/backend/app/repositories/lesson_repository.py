from typing import List, Optional, Dict, Any
from motor.motor_asyncio import AsyncIOMotorDatabase

class LessonRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db.lessons

    async def get_by_slug(self, slug: str) -> Optional[dict]:
        return await self.collection.find_one({"slug": slug})

    async def get_by_course(self, course_slug: str) -> List[dict]:
        cursor = self.collection.find({"course_slug": course_slug}).sort("order", 1)
        return await cursor.to_list(length=200)

    async def create_or_update(self, lesson_doc: dict) -> dict:
        await self.collection.update_one(
            {"slug": lesson_doc["slug"]},
            {"$set": lesson_doc},
            upsert=True
        )
        return await self.get_by_slug(lesson_doc["slug"])
