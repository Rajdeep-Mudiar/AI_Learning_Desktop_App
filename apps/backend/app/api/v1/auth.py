from fastapi import APIRouter, Depends, status
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.core.database import get_database
from app.api.deps import get_current_user
from app.schemas.user import UserCreate, UserLogin, UserProfileUpdate, UserOut, TokenResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserCreate, db: AsyncIOMotorDatabase = Depends(get_database)):
    service = AuthService(db)
    user_doc, token = await service.register(user_in)
    return TokenResponse(
        access_token=token,
        token_type="bearer",
        user=UserOut(**user_doc)
    )

@router.post("/login", response_model=TokenResponse)
async def login(login_in: UserLogin, db: AsyncIOMotorDatabase = Depends(get_database)):
    service = AuthService(db)
    user_doc, token = await service.login(login_in)
    return TokenResponse(
        access_token=token,
        token_type="bearer",
        user=UserOut(**user_doc)
    )

@router.get("/me", response_model=UserOut)
async def get_me(current_user: dict = Depends(get_current_user), db: AsyncIOMotorDatabase = Depends(get_database)):
    service = AuthService(db)
    user_doc = await service.get_profile(current_user)
    return UserOut(**user_doc)

@router.put("/profile", response_model=UserOut)
async def update_profile(
    update_data: UserProfileUpdate,
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    service = AuthService(db)
    updated_user = await service.update_profile(current_user, update_data)
    return UserOut(**updated_user)
