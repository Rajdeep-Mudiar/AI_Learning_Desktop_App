from typing import List, Dict, Any, Optional
from pydantic import BaseModel

class Point2D(BaseModel):
    x: float
    y: float
    label: Optional[int] = None

class RegressionStepRequest(BaseModel):
    points: List[Point2D]
    weight: float
    bias: float
    learning_rate: float = 0.05

class RegressionStepResponse(BaseModel):
    new_weight: float
    new_bias: float
    mse_loss: float
    gradient_w: float
    gradient_b: float
    residuals: List[float]

class KMeansStepRequest(BaseModel):
    points: List[Point2D]
    centroids: List[Point2D]

class KMeansStepResponse(BaseModel):
    assignments: List[int]
    new_centroids: List[Point2D]
    inertia: float
    converged: bool

class PCARequest(BaseModel):
    points: List[Point2D]

class PCAResponse(BaseModel):
    mean: Point2D
    components: List[Point2D]
    eigenvalues: List[float]
    explained_variance_ratio: List[float]
    projected_points: List[Point2D]
