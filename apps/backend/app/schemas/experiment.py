from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class PreprocessingConfig(BaseModel):
    imputation: str = "mean"  # "mean", "median", "drop", "none"
    scaling: str = "standard"  # "standard", "minmax", "robust", "none"
    test_size: float = Field(default=0.2, ge=0.05, le=0.5)
    random_state: int = 42

class TrainExperimentRequest(BaseModel):
    dataset_id: str
    model_type: str  # "logistic_regression", "random_forest_classifier", "svm_classifier", "knn_classifier", "decision_tree_classifier", "linear_regression", "ridge_regression", "random_forest_regressor", "knn_regressor"
    task_type: str = "classification"  # "classification", "regression"
    hyperparameters: Dict[str, Any] = Field(default_factory=dict)
    preprocessing: PreprocessingConfig = Field(default_factory=PreprocessingConfig)
    feature_selection: Optional[List[str]] = None
    experiment_name: Optional[str] = None

class ConfusionMatrixData(BaseModel):
    labels: List[str]
    matrix: List[List[int]]

class ROCPoint(BaseModel):
    fpr: float
    tpr: float

class ROCCurveData(BaseModel):
    points: List[ROCPoint]
    auc: float

class MetricsSummary(BaseModel):
    accuracy: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None
    f1_score: Optional[float] = None
    mse: Optional[float] = None
    rmse: Optional[float] = None
    mae: Optional[float] = None
    r2_score: Optional[float] = None
    training_time_ms: float = 0.0
    train_score: Optional[float] = None
    test_score: Optional[float] = None

class FeatureImportance(BaseModel):
    feature: str
    importance: float

class ExperimentResult(BaseModel):
    id: str
    user_id: Optional[str] = None
    experiment_name: str
    dataset_id: str
    model_type: str
    task_type: str
    hyperparameters: Dict[str, Any]
    preprocessing: PreprocessingConfig
    metrics: MetricsSummary
    confusion_matrix: Optional[ConfusionMatrixData] = None
    roc_curve: Optional[ROCCurveData] = None
    feature_importances: List[FeatureImportance] = Field(default_factory=list)
    created_at: str

class ExperimentCompareResponse(BaseModel):
    experiments: List[ExperimentResult]
