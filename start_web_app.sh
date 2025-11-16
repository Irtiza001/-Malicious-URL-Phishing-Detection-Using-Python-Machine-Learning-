#!/bin/bash
# Linux/Mac Shell Script to Start Web Application

echo "Starting URL Phishing Detection Web Application..."
echo ""

# Activate virtual environment
source venv/bin/activate

# Check if activation was successful
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to activate virtual environment"
    echo "Make sure venv exists and is properly set up"
    exit 1
fi

# Start the Flask server
python start_web_app.py

