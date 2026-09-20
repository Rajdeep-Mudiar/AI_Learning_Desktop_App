@echo off
echo ========================================================
echo   Building AI Learning Lab Production Distribution
echo ========================================================

echo.
echo [1/2] Checking Python Virtual Environment...
cd /d %~dp0..\apps\backend
if not exist ".\venv\Scripts\python.exe" (
    echo [ERROR] Python virtual environment not found in apps/backend/venv!
    pause
    exit /b 1
)

echo [2/2] Building Vite Frontend Distribution Assets...
cd /d %~dp0..\apps\desktop
call npm run build
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Frontend build failed!
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo ========================================================
echo   Build Successful! Production assets ready in apps/desktop/dist
echo   To launch full desktop environment: scripts\start_dev.bat
echo ========================================================
pause
