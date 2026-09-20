from typing import Optional, Tuple
from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserLogin, UserProfileUpdate, UserOut
from app.core.security import verify_password, get_password_hash, create_access_token

class AuthService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.user_repo = UserRepository(db)

    async def register(self, user_in: UserCreate) -> Tuple[dict, str]:
        existing_user = await self.user_repo.get_by_email(user_in.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="An account with this email address already exists."
            )
        
        password_hash = get_password_hash(user_in.password)
        user_doc = await self.user_repo.create(user_in, password_hash)
        
        user_id = str(user_doc["_id"])
        access_token = create_access_token(user_id)
        
        user_doc["id"] = user_id
        return user_doc, access_token

    async def login(self, login_in: UserLogin) -> Tuple[dict, str]:
        user_doc = await self.user_repo.get_by_email(login_in.email)
        if not user_doc:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password."
            )
        
        if not verify_password(login_in.password, user_doc["password_hash"]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password."
            )
            
        user_id = str(user_doc["_id"])
        await self.user_repo.update_streak(user_id)
        # Re-fetch with updated streak
        user_doc = await self.user_repo.get_by_id(user_id)
        user_doc["id"] = user_id
        access_token = create_access_token(user_id)
        return user_doc, access_token

    async def get_profile(self, user: dict) -> dict:
        user_id = str(user["_id"])
        user_doc = await self.user_repo.get_by_id(user_id)
        user_doc["id"] = user_id
        return user_doc

    async def update_profile(self, user: dict, update_data: UserProfileUpdate) -> dict:
        user_id = str(user["_id"])
        updated = await self.user_repo.update_profile(user_id, update_data)
        updated["id"] = user_id
        return updated
