@echo off
echo Resetting and Seeding AI Learning Lab Curriculum Database...
cd /d %~dp0..\apps\backend
.\venv\Scripts\python.exe -m app.seed.seed_runner
pause
