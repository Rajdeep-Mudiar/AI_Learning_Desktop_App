@echo off
echo ========================================================
echo   Starting AI Learning Lab (FastAPI Backend + React UI)
echo ========================================================

:: Start FastAPI Backend
start "AI Learning Lab - Backend" cmd /k "cd /d %~dp0..\apps\backend && .\venv\Scripts\python.exe main.py"

:: Start Vite Frontend
start "AI Learning Lab - Frontend" cmd /k "cd /d %~dp0..\apps\desktop && npm run dev"

echo Backend running at: http://127.0.0.1:8001
echo Frontend running at: http://localhost:5173
echo.
