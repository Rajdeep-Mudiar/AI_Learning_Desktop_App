from fastapi import APIRouter
from app.schemas.sandbox import CodeExecutionRequest, CodeExecutionResponse
from app.sandbox.executor import SandboxExecutor

router = APIRouter(prefix="/sandbox", tags=["Sandbox"])

@router.post("/execute", response_model=CodeExecutionResponse)
async def execute_code(req: CodeExecutionRequest):
    return await SandboxExecutor.execute_code(req)
