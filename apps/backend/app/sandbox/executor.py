import asyncio
import os
import sys
import time
import uuid
import shutil
import tempfile
import subprocess
from app.schemas.sandbox import CodeExecutionRequest, CodeExecutionResponse

MAX_OUTPUT_CHARS = 50_000

class SandboxExecutor:
    @staticmethod
    def _run_subprocess_sync(temp_dir: str, main_script: str, req: CodeExecutionRequest, exec_id: str) -> CodeExecutionResponse:
        python_bin = sys.executable
        start_time = time.perf_counter()
        
        try:
            completed_proc = subprocess.run(
                [python_bin, main_script],
                cwd=temp_dir,
                input=req.stdin_input if req.stdin_input else None,
                capture_output=True,
                text=True,
                timeout=req.timeout_seconds,
                encoding="utf-8",
                errors="replace",
                env={
                    **os.environ,
                    "PYTHONIOENCODING": "utf-8",
                    "PYTHONUNBUFFERED": "1",
                }
            )
            end_time = time.perf_counter()
            duration_ms = round((end_time - start_time) * 1000.0, 2)
            
            stdout_str = (completed_proc.stdout or "")[:MAX_OUTPUT_CHARS]
            stderr_str = (completed_proc.stderr or "")[:MAX_OUTPUT_CHARS]
            exit_code = completed_proc.returncode
            status_str = "success" if exit_code == 0 else "error"
            
            return CodeExecutionResponse(
                execution_id=exec_id,
                status=status_str,
                stdout=stdout_str,
                stderr=stderr_str,
                exit_code=exit_code,
                duration_ms=duration_ms,
                memory_mb=None
            )
        except subprocess.TimeoutExpired:
            end_time = time.perf_counter()
            duration_ms = round((end_time - start_time) * 1000.0, 2)
            return CodeExecutionResponse(
                execution_id=exec_id,
                status="timeout",
                stdout="",
                stderr=f"Execution timed out after {req.timeout_seconds} seconds. Check for infinite loops.",
                exit_code=-1,
                duration_ms=duration_ms,
                memory_mb=None
            )
        except Exception as e:
            return CodeExecutionResponse(
                execution_id=exec_id,
                status="error",
                stdout="",
                stderr=f"Sandbox Execution Error: {str(e)}",
                exit_code=-1,
                duration_ms=0.0
            )

    @classmethod
    async def execute_code(cls, req: CodeExecutionRequest) -> CodeExecutionResponse:
        exec_id = str(uuid.uuid4())
        temp_dir = tempfile.mkdtemp(prefix=f"ailearn_sandbox_{exec_id}_")
        main_script = os.path.join(temp_dir, "main.py")

        try:
            # Write multi-file files if supplied
            if req.filenames:
                for fname, fcontent in req.filenames.items():
                    safe_name = os.path.basename(fname)
                    fpath = os.path.join(temp_dir, safe_name)
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(fcontent)

            # Write main.py
            with open(main_script, "w", encoding="utf-8") as f:
                f.write(req.code)

            return await asyncio.to_thread(cls._run_subprocess_sync, temp_dir, main_script, req, exec_id)

        except Exception as e:
            return CodeExecutionResponse(
                execution_id=exec_id,
                status="error",
                stdout="",
                stderr=f"Sandbox Setup Error: {str(e)}",
                exit_code=-1,
                duration_ms=0.0
            )

        finally:
            # Clean up temp sandbox directory
            try:
                shutil.rmtree(temp_dir, ignore_errors=True)
            except Exception:
                pass
