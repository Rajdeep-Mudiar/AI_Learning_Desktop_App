from fastapi import APIRouter
from typing import List
from app.schemas.interview import (
    HackathonChallenge,
    LeaderboardEntry,
    HackathonSubmissionRequest
)
from app.services.interview_service import (
    list_hackathons,
    submit_hackathon_entry
)

router = APIRouter(prefix="/hackathons", tags=["Hackathons"])

@router.get("", response_model=List[HackathonChallenge])
async def get_hackathons():
    """Retrieve active and upcoming AI hackathon challenges."""
    return list_hackathons()

@router.post("/submit", response_model=LeaderboardEntry)
async def submit_hackathon(req: HackathonSubmissionRequest):
    """Submit code to a timed hackathon challenge and update live leaderboard ranking."""
    return submit_hackathon_entry(req)
