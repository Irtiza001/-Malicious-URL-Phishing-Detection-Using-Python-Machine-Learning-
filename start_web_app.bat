@echo off
REM Windows Batch Script to Start Web Application
echo Starting URL Phishing Detection Web Application...
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Check if activation was successful
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    echo Make sure venv exists and is properly set up
    pause
    exit /b 1
)

REM Start the Flask server
python start_web_app.py

pause

