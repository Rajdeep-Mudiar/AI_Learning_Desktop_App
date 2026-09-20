from fastapi import APIRouter, HTTPException
from typing import List, Dict
from pydantic import BaseModel
from app.schemas.interview import (
    InterviewTrack,
    InterviewReport
)
from app.services.interview_service import (
    list_interview_tracks,
    get_track_by_id,
    evaluate_interview_session
)

router = APIRouter(prefix="/interviews", tags=["Interviews"])

class SubmitAnswersPayload(BaseModel):
    answers: List[Dict[str, str]]

@router.get("/tracks", response_model=List[InterviewTrack])
async def get_tracks():
    """Retrieve full catalog of AI & ML engineering interview tracks."""
    return list_interview_tracks()

@router.get("/tracks/{track_id}", response_model=InterviewTrack)
async def get_track(track_id: str):
    """Retrieve questions and rubrics for a specific interview track."""
    t = get_track_by_id(track_id)
    if not t:
        raise HTTPException(status_code=404, detail="Interview track not found")
    return t

@router.post("/tracks/{track_id}/evaluate", response_model=InterviewReport)
async def evaluate_interview(track_id: str, payload: SubmitAnswersPayload):
    """Evaluate interview answers, generate hiring recommendation, and provide rubric feedback."""
    return evaluate_interview_session(track_id, payload.answers)
