@echo off
echo ========================================================
echo   Running AI Learning Lab Test and Verification Suite
echo ========================================================

echo.
echo [1/2] Running Backend Pytest Suite (All 11 Phases)...
cd /d %~dp0..\apps\backend
set PYTHONPATH=%cd%
.\venv\Scripts\pytest.exe ..\..\tests -v
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Backend tests failed!
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo [2/2] Running Desktop Frontend Production Build...
cd /d %~dp0..\apps\desktop
call npm run build
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Frontend build failed!
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo ========================================================
echo   SUCCESS: All 11 Phases Verified and 100%% Operational!
echo ========================================================
pause
