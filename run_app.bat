@echo off
echo ========================================
echo Smart Expense Visualizer
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "myenv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Please run "setup_portable.bat" first to set up the environment.
    pause
    exit /b 1
)

echo Activating virtual environment...
call myenv\Scripts\activate.bat

echo.
echo Starting Smart Expense Visualizer...
echo The app will open in your default web browser.
echo.
echo To stop the app, close this window or press Ctrl+C
echo.

streamlit run app.py --server.headless false --server.port 8501
