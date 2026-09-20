from typing import List
from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.core.database import get_database
from app.api.deps import get_current_user
from app.schemas.challenge import (
    ChallengeSummary, ChallengeDetail,
    ChallengeSubmissionRequest, ChallengeSubmissionResponse
)
from app.services.challenge_service import ChallengeService

router = APIRouter(prefix="/challenges", tags=["Challenges"])

@router.get("", response_model=List[ChallengeSummary])
async def list_challenges():
    return ChallengeService.list_challenges()

@router.get("/{challenge_id}", response_model=ChallengeDetail)
async def get_challenge(challenge_id: str):
    return ChallengeService.get_challenge(challenge_id)

@router.post("/{challenge_id}/submit", response_model=ChallengeSubmissionResponse)
async def submit_challenge(
    challenge_id: str,
    submission: ChallengeSubmissionRequest,
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    submission.challenge_id = challenge_id
    user_id = str(current_user["_id"])
    return await ChallengeService.grade_submission(submission, user_id, db)
