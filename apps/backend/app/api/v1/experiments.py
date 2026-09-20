from fastapi import APIRouter, HTTPException, Depends
from typing import List
from pydantic import BaseModel
from app.schemas.experiment import (
    TrainExperimentRequest,
    ExperimentResult,
    ExperimentCompareResponse
)
from app.services.experiment_service import (
    train_and_evaluate_experiment,
    get_user_experiments,
    compare_experiments
)

router = APIRouter(prefix="/experiments", tags=["Experiments"])

class CompareRequest(BaseModel):
    experiment_ids: List[str]

@router.post("/train", response_model=ExperimentResult)
async def run_experiment(req: TrainExperimentRequest):
    """Train a scikit-learn model, perform validation, and calculate metrics."""
    try:
        return await train_and_evaluate_experiment(req)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model training failed: {str(e)}")

@router.get("", response_model=List[ExperimentResult])
async def list_experiments():
    """Retrieve history of saved experiments."""
    return await get_user_experiments()

@router.post("/compare", response_model=ExperimentCompareResponse)
async def compare_experiment_run(req: CompareRequest):
    """Compare multiple experiment runs side-by-side."""
    exps = await compare_experiments(req.experiment_ids)
    return ExperimentCompareResponse(experiments=exps)
