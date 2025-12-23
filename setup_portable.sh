#!/bin/bash

echo "========================================"
echo "Smart Expense Visualizer - Portable Setup"
echo "========================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.8+ from https://python.org"
    exit 1
fi

echo "Python found! Checking version..."
python3 --version

echo
echo "Creating virtual environment..."
python3 -m venv myenv

echo
echo "Activating virtual environment..."
source myenv/bin/activate

echo
echo "Installing required packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo
echo "To run the app:"
echo "1. Run: ./run_app.sh"
echo "2. Or run: source myenv/bin/activate && streamlit run app.py"
echo
echo "The app will open in your default web browser."
echo
