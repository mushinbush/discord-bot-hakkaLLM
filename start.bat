@echo off

cd "%~dp0"
title Gemini Discord Bot

:: venv check
if not exist "venv\" (
    echo No venv found! Create venv and install dependencies now.
    python -m venv venv
    call .\venv\Scripts\activate.bat
    echo Installing dependencies from requirements.txt
    call pip install -r requirements.txt
    call python discordbot_gemini.py
    pause
) else (
    call .\venv\Scripts\activate.bat
    call python discordbot_gemini.py
    pause
)