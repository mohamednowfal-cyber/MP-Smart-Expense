@echo off
echo Activating virtual environment...
call myenv\Scripts\activate.bat
echo Virtual environment activated!
echo You can now run: streamlit run app.py
cmd /k
