#!/usr/bin/env bash
# Create a .venv with the system default python3 (assumes python3 is the desired latest)
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Virtualenv created at .venv and dependencies installed. Activate with: source .venv/bin/activate"
