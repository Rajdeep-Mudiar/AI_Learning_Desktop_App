from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field

class CodeExecutionRequest(BaseModel):
    code: str = Field(..., min_length=1)
    timeout_seconds: float = Field(default=5.0, ge=1.0, le=15.0)
    stdin_input: Optional[str] = None
    filenames: Optional[Dict[str, str]] = None  # Multi-file support: {"helper.py": "..."}

class CodeExecutionResponse(BaseModel):
    execution_id: str
    status: str  # success, error, timeout
    stdout: str
    stderr: str
    exit_code: int
    duration_ms: float
    memory_mb: Optional[float] = None
