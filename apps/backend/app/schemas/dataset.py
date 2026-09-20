from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class ColumnSummary(BaseModel):
    name: str
    data_type: str
    count: int
    missing_count: int
    missing_ratio: float
    mean: Optional[float] = None
    std: Optional[float] = None
    min: Optional[float] = None
    q25: Optional[float] = None
    median: Optional[float] = None
    q75: Optional[float] = None
    max: Optional[float] = None
    unique_count: int
    sample_values: List[Any] = Field(default_factory=list)
    skewness: Optional[float] = None

class CorrelationMatrix(BaseModel):
    features: List[str]
    matrix: List[List[float]]

class DiagnosticWarning(BaseModel):
    severity: str  # "info", "warning", "critical"
    title: str
    description: str
    recommendation: str
    affected_columns: List[str] = Field(default_factory=list)

class DatasetListItem(BaseModel):
    id: str
    name: str
    description: str
    task_type: str  # "classification", "regression", "clustering"
    num_rows: int
    num_columns: int
    target_column: Optional[str] = None
    tags: List[str] = Field(default_factory=list)

class DatasetProfileResponse(BaseModel):
    id: str
    name: str
    description: str
    task_type: str
    num_rows: int
    num_columns: int
    target_column: Optional[str] = None
    features: List[str]
    columns_summary: List[ColumnSummary]
    correlation_matrix: Optional[CorrelationMatrix] = None
    diagnostic_warnings: List[DiagnosticWarning] = Field(default_factory=list)
    sample_rows: List[Dict[str, Any]] = Field(default_factory=list)
    class_distribution: Optional[Dict[str, int]] = None

class CustomDatasetUploadRequest(BaseModel):
    name: str
    description: Optional[str] = "User uploaded dataset"
    task_type: str = "classification"
    target_column: Optional[str] = None
    csv_content: str
