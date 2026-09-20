from datetime import datetime, timezone
from typing import Optional, Dict, Any, List
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.schemas.user import UserCreate, UserProfileUpdate

class UserRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db.users

    async def get_by_id(self, user_id: str) -> Optional[dict]:
        try:
            return await self.collection.find_one({"_id": ObjectId(user_id)})
        except Exception:
            return await self.collection.find_one({"_id": user_id})

    async def get_by_email(self, email: str) -> Optional[dict]:
        return await self.collection.find_one({"email": email.lower()})

    async def create(self, user_in: UserCreate, password_hash: str) -> dict:
        now = datetime.now(timezone.utc)
        
        # Initial default skills matrix
        initial_skills = {
            "python_basics": 10.0,
            "numpy_basics": 0.0,
            "pandas_basics": 0.0,
            "linear_algebra": 0.0,
            "calculus": 0.0,
            "statistics": 0.0,
            "supervised_learning": 0.0,
            "regression": 0.0,
            "classification": 0.0,
            "neural_networks": 0.0,
            "deep_learning": 0.0,
            "transformers": 0.0,
            "rag": 0.0
        }
        
        doc = {
            "name": user_in.name,
            "email": user_in.email.lower(),
            "password_hash": password_hash,
            "role": "student",
            "avatar_url": f"https://api.dicebear.com/7.x/bottts/svg?seed={user_in.name}",
            "skill_mastery": initial_skills,
            "streak": {
                "current": 1,
                "longest": 1,
                "last_active_date": now.strftime("%Y-%m-%d"),
                "completed_challenges_count": 0
            },
            "learning_preferences": {
                "theme": "dark",
                "daily_goal_mins": 30,
                "preferred_track": user_in.preferred_track or "ai_engineer",
                "notifications_enabled": True
            },
            "created_at": now,
            "updated_at": now
        }
        result = await self.collection.insert_one(doc)
        doc["_id"] = result.inserted_id
        return doc

    async def update_profile(self, user_id: str, update_data: UserProfileUpdate) -> Optional[dict]:
        update_fields = {"updated_at": datetime.now(timezone.utc)}
        if update_data.name is not None:
            update_fields["name"] = update_data.name
        if update_data.avatar_url is not None:
            update_fields["avatar_url"] = update_data.avatar_url
        if update_data.learning_preferences is not None:
            update_fields["learning_preferences"] = update_data.learning_preferences.model_dump()
            
        try:
            query = {"_id": ObjectId(user_id)}
        except Exception:
            query = {"_id": user_id}
            
        await self.collection.update_one(query, {"$set": update_fields})
        return await self.get_by_id(user_id)

    async def update_skill_mastery(self, user_id: str, skill_tag: str, delta: float) -> dict:
        user = await self.get_by_id(user_id)
        if not user:
            return {}
        
        mastery = user.get("skill_mastery", {})
        current = mastery.get(skill_tag, 0.0)
        new_val = max(0.0, min(100.0, current + delta))
        mastery[skill_tag] = round(new_val, 1)
        
        try:
            query = {"_id": ObjectId(user_id)}
        except Exception:
            query = {"_id": user_id}
            
        await self.collection.update_one(
            query, 
            {"$set": {"skill_mastery": mastery, "updated_at": datetime.now(timezone.utc)}}
        )
        return mastery

    async def update_streak(self, user_id: str) -> dict:
        user = await self.get_by_id(user_id)
        if not user:
            return {}
            
        streak = user.get("streak", {"current": 1, "longest": 1, "last_active_date": ""})
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        last_date = streak.get("last_active_date")
        
        if last_date != today:
            # Check if yesterday or first time
            current = streak.get("current", 1)
            longest = streak.get("longest", 1)
            if last_date:
                try:
                    last_dt = datetime.strptime(last_date, "%Y-%m-%d").date()
                    now_dt = datetime.now(timezone.utc).date()
                    diff = (now_dt - last_dt).days
                    if diff == 1:
                        current += 1
                        if current > longest:
                            longest = current
                    elif diff > 1:
                        current = 1
                except Exception:
                    pass
            streak["current"] = current
            streak["longest"] = longest
            streak["last_active_date"] = today
            
            try:
                query = {"_id": ObjectId(user_id)}
            except Exception:
                query = {"_id": user_id}
                
            await self.collection.update_one(query, {"$set": {"streak": streak}})
            
        return streak
