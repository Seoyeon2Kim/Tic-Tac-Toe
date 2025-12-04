@echo off
setlocal enabledelayedexpansion

echo Running the program!

if exist ".venv\Scripts\activate.bat" (
    call ".venv\Scripts\activate.bat"
)

python -m pip install -r requirements.txt
python src\main.py
