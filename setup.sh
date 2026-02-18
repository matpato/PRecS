#!/bin/bash
set -e

if [ ! -d "venv" ]; then
    echo "Creating virtual environment."
    python3 -m venv venv
fi

echo "Activating virtual environment."
source venv/bin/activate

echo "Installing dependencies."
pip install -r requirements.txt

echo "Starting server."
uvicorn main:app --reload