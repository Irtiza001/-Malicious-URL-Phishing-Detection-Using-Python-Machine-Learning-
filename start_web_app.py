#!/usr/bin/env python
"""
Quick Start Script for Web Application
Starts the Flask API server with proper setup
"""

import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.absolute()
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Check if model exists
model_path = project_root / 'models' / 'best_model.pkl'
if not model_path.exists():
    print("=" * 60)
    print("⚠️  WARNING: Model file not found!")
    print("=" * 60)
    print(f"Expected model at: {model_path}")
    print("\nPlease train a model first by running:")
    print("  python train.py")
    print("\nThis will create the required model file.")
    print("=" * 60)
    
    response = input("\nDo you want to continue anyway? (y/n): ").strip().lower()
    if response != 'y':
        print("Exiting. Please train a model first.")
        sys.exit(1)

# Import and run the Flask app
try:
    from api.app import app, load_classifier
    
    print("\n" + "=" * 60)
    print("Starting URL Phishing Detection Web Application")
    print("=" * 60)
    
    # Load classifier
    if not load_classifier():
        print("\n❌ ERROR: Failed to load classifier. Exiting.")
        sys.exit(1)
    
    print("\n✅ Backend API Server Starting...")
    print("📍 API URL: http://localhost:5000")
    print("🌐 Frontend: Open frontend/index.html in your browser")
    print("\n💡 Tip: Keep this window open while using the web app")
    print("   Press CTRL+C to stop the server")
    print("=" * 60 + "\n")
    
    # Run the app
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        threaded=True
    )
    
except ImportError as e:
    print(f"\n❌ Import Error: {e}")
    print("\nMake sure you're in the project root directory and all dependencies are installed:")
    print("  pip install -r requirements.txt")
    sys.exit(1)
except KeyboardInterrupt:
    print("\n\n👋 Server stopped. Goodbye!")
    sys.exit(0)
except Exception as e:
    print(f"\n❌ Error starting server: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
