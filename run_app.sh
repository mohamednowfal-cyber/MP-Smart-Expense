#!/bin/bash

echo "========================================"
echo "Smart Expense Visualizer"
echo "========================================"
echo

# Check if virtual environment exists
if [ ! -f "myenv/bin/activate" ]; then
    echo "ERROR: Virtual environment not found!"
    echo "Please run './setup_portable.sh' first to set up the environment."
    exit 1
fi

echo "Activating virtual environment..."
source myenv/bin/activate

echo
echo "Starting Smart Expense Visualizer..."
echo "The app will open in your default web browser."
echo
echo "To stop the app, close this window or press Ctrl+C"
echo

streamlit run app.py --server.headless false --server.port 8501
