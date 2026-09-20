from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.core.database import get_database
from app.api.deps import get_current_user
from app.schemas.quiz import QuizDetail, QuizSubmissionRequest, QuizSubmissionResponse
from app.services.quiz_service import QuizService

router = APIRouter(prefix="/quizzes", tags=["Quizzes"])

@router.get("/{quiz_id}", response_model=QuizDetail)
async def get_quiz(quiz_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    service = QuizService(db)
    return await service.get_quiz_for_student(quiz_id)

@router.post("/{quiz_id}/submit", response_model=QuizSubmissionResponse)
async def submit_quiz(
    quiz_id: str,
    submission: QuizSubmissionRequest,
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    service = QuizService(db)
    user_id = str(current_user["_id"])
    return await service.grade_submission(quiz_id, submission, user_id)
