#!/bin/bash

cd "$(dirname "$0")" || exit

if [ ! -d "venv" ]; then
    echo "No venv found! Create venv and install dependencies now."
    python3 -m venv venv
    source venv/bin/activate
    echo "Installing dependencies from requirements.txt"
    pip install -r requirements.txt
    python3 discordbot_hakka.py
else
    source venv/bin/activate
    python3 discordbot_hakka.py
fi