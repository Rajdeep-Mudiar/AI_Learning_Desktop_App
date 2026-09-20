from typing import List
from fastapi import APIRouter, Depends
from app.api.deps import get_current_user
from app.schemas.diagnostic import (
    DiagnosticScenarioSummary, DiagnosticScenarioDetail,
    DiagnosticSubmissionRequest, DiagnosticSubmissionResponse
)
from app.services.diagnostic_service import DiagnosticService

router = APIRouter(prefix="/diagnostics", tags=["Diagnostics"])

@router.get("/scenarios", response_model=List[DiagnosticScenarioSummary])
async def list_diagnostic_scenarios():
    return DiagnosticService.list_scenarios()

@router.get("/scenarios/{scenario_id}", response_model=DiagnosticScenarioDetail)
async def get_diagnostic_scenario(scenario_id: str):
    return DiagnosticService.get_scenario(scenario_id)

@router.post("/scenarios/{scenario_id}/submit", response_model=DiagnosticSubmissionResponse)
async def submit_diagnosis(
    scenario_id: str,
    submission: DiagnosticSubmissionRequest,
    current_user: dict = Depends(get_current_user)
):
    submission.scenario_id = scenario_id
    return DiagnosticService.evaluate_diagnosis(submission)
