from fastapi import APIRouter
from app.schemas.simulation import (
    RegressionStepRequest, RegressionStepResponse,
    KMeansStepRequest, KMeansStepResponse,
    PCARequest, PCAResponse
)
from app.services.simulation_service import SimulationService

router = APIRouter(prefix="/simulations", tags=["Simulations"])

@router.post("/linear-regression/step", response_model=RegressionStepResponse)
async def step_linear_regression(req: RegressionStepRequest):
    return SimulationService.step_linear_regression(req)

@router.post("/kmeans/step", response_model=KMeansStepResponse)
async def step_kmeans(req: KMeansStepRequest):
    return SimulationService.step_kmeans(req)

@router.post("/pca/compute", response_model=PCAResponse)
async def compute_pca(req: PCARequest):
    return SimulationService.compute_pca(req)
