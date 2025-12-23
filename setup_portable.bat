@echo off
echo ========================================
echo Smart Expense Visualizer - Portable Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python found! Checking version...
python --version

echo.
echo Creating virtual environment...
python -m venv myenv

echo.
echo Activating virtual environment...
call myenv\Scripts\activate.bat

echo.
echo Installing required packages...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To run the app:
echo 1. Double-click "run_app.bat"
echo 2. Or run: myenv\Scripts\activate && streamlit run app.py
echo.
echo The app will open in your default web browser.
echo.
pause
