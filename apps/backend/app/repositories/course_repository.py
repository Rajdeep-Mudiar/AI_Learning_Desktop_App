from typing import List, Optional, Dict, Any
from motor.motor_asyncio import AsyncIOMotorDatabase

class CourseRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db.courses
        self.lessons_collection = db.lessons

    async def get_all(self) -> List[dict]:
        cursor = self.collection.find({"is_published": True}).sort("order", 1)
        return await cursor.to_list(length=100)

    async def get_by_slug(self, slug: str) -> Optional[dict]:
        return await self.collection.find_one({"slug": slug})

    async def get_course_lessons(self, course_slug: str) -> List[dict]:
        # First query by course_slug
        lessons = await self.lessons_collection.find({"course_slug": course_slug}).sort("order", 1).to_list(length=200)
        if not lessons:
            course = await self.get_by_slug(course_slug)
            if course:
                c_id = course.get("id") or course.get("slug")
                lessons = await self.lessons_collection.find({
                    "$or": [
                        {"course_slug": course_slug},
                        {"course_id": c_id},
                        {"course_id": course_slug},
                        {"course_slug": c_id}
                    ]
                }).sort("order", 1).to_list(length=200)
        return lessons

    async def create_or_update(self, course_doc: dict) -> dict:
        await self.collection.update_one(
            {"slug": course_doc["slug"]},
            {"$set": course_doc},
            upsert=True
        )
        return await self.get_by_slug(course_doc["slug"])
