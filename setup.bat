@echo off

if not exist venv (
    echo Creating virtual environment.
    python -m venv venv
)

echo Activating virtual environment.
call venv\Scripts\activate

echo Installing dependencies.
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo Installation failed.
    pause
    exit /b
)

echo Starting server.
uvicorn main:app --reload