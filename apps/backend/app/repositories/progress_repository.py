from datetime import datetime, timezone
from typing import List, Optional, Dict, Any
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase

class ProgressRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db.progress

    async def get_user_course_progress(self, user_id: str, course_slug: str) -> Optional[dict]:
        return await self.collection.find_one({"user_id": str(user_id), "course_slug": course_slug})

    async def get_all_user_progress(self, user_id: str) -> List[dict]:
        cursor = self.collection.find({"user_id": str(user_id)})
        return await cursor.to_list(length=100)

    async def mark_lesson_completed(self, user_id: str, course_slug: str, lesson_slug: str, total_lessons: int) -> dict:
        now = datetime.now(timezone.utc)
        record = await self.get_user_course_progress(user_id, course_slug)
        
        completed_lessons = set()
        quiz_scores = {}
        if record:
            completed_lessons = set(record.get("completed_lessons", []))
            quiz_scores = record.get("quiz_scores", {})
            
        completed_lessons.add(lesson_slug)
        completed_list = list(completed_lessons)
        percentage = round((len(completed_list) / max(1, total_lessons)) * 100.0, 1)
        
        doc = {
            "user_id": str(user_id),
            "course_slug": course_slug,
            "completed_lessons": completed_list,
            "last_lesson_slug": lesson_slug,
            "percentage": min(100.0, percentage),
            "quiz_scores": quiz_scores,
            "updated_at": now
        }
        
        await self.collection.update_one(
            {"user_id": str(user_id), "course_slug": course_slug},
            {"$set": doc},
            upsert=True
        )
        return doc

    async def record_quiz_result(self, user_id: str, course_slug: str, quiz_id: str, score: int, max_score: int, passed: bool) -> dict:
        now = datetime.now(timezone.utc)
        record = await self.get_user_course_progress(user_id, course_slug)
        
        completed_lessons = []
        quiz_scores = {}
        percentage = 0.0
        last_lesson = None
        
        if record:
            completed_lessons = record.get("completed_lessons", [])
            quiz_scores = record.get("quiz_scores", {})
            percentage = record.get("percentage", 0.0)
            last_lesson = record.get("last_lesson_slug")
            
        prev_attempts = quiz_scores.get(quiz_id, {}).get("attempts", 0)
        quiz_scores[quiz_id] = {
            "score": score,
            "max_score": max_score,
            "percentage": round((score / max(1, max_score)) * 100.0, 1),
            "passed": passed,
            "attempts": prev_attempts + 1,
            "last_attempt_date": now.isoformat()
        }
        
        doc = {
            "user_id": str(user_id),
            "course_slug": course_slug,
            "completed_lessons": completed_lessons,
            "last_lesson_slug": last_lesson,
            "percentage": percentage,
            "quiz_scores": quiz_scores,
            "updated_at": now
        }
        
        await self.collection.update_one(
            {"user_id": str(user_id), "course_slug": course_slug},
            {"$set": doc},
            upsert=True
        )
        return doc
