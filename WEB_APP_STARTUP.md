# Web Application - Quick Start Guide

## 🚀 Running the Web Application

Your URL Phishing Detection System now has a complete web interface! Follow these simple steps to get it running.

### Prerequisites

1. **Trained Model**: Make sure you have trained a model first:
   ```bash
   python train.py
   ```
   This creates `models/best_model.pkl` which the web app needs.

2. **Dependencies**: All dependencies are already installed in your virtual environment.

### Step 1: Start the Backend API Server

Open a terminal/command prompt in the project root directory and run:

```bash
# Activate virtual environment (if not already activated)
.\venv\Scripts\Activate.ps1    # Windows PowerShell
# or
venv\Scripts\activate.bat      # Windows CMD
# or
source venv/bin/activate       # Linux/Mac

# Start the Flask API server
python api/app.py
```

You should see:
```
============================================================
URL Phishing Detection API Server
============================================================
Loading model from C:\Users\Hp\Desktop\IS\models\best_model.pkl...
Model loaded successfully: [Model Name]

Starting Flask server...
API will be available at: http://localhost:5000
Endpoints:
  GET  /health  - Health check
  POST /predict - Classify a single URL
  POST /predict/batch - Classify multiple URLs

Press CTRL+C to stop the server
============================================================
 * Running on http://0.0.0.0:5000
```

**Keep this terminal window open** - the server needs to keep running.

### Step 2: Open the Frontend

1. **Option A: Direct File Opening**
   - Navigate to the `frontend` folder
   - Double-click `index.html` to open it in your default browser
   - Or right-click → "Open with" → Choose your browser

2. **Option B: Using a Local Server (Recommended)**
   - If you have Python installed, you can run a simple HTTP server:
   ```bash
   # In a NEW terminal window, navigate to the frontend folder
   cd frontend
   
   # Python 3
   python -m http.server 8000
   
   # Then open: http://localhost:8000
   ```

### Step 3: Use the Web Application

1. The web interface will load in your browser
2. Enter a URL in the input box (e.g., `https://example.com`)
3. Click "Check Safety" button
4. View the results:
   - Prediction (Benign/Malicious)
   - Confidence score
   - Probability breakdown
5. Check your history of recent URL checks below

### Features

✅ **Clean, Modern UI** - Professional design with smooth animations  
✅ **Dark/Light Theme** - Toggle theme using the moon/sun icon in the header  
✅ **Real-time Classification** - Instant results from your ML model  
✅ **History Tracking** - View and reuse your recent URL checks  
✅ **Responsive Design** - Works on desktop, tablet, and mobile  
✅ **Error Handling** - Clear error messages for invalid URLs or API issues  
✅ **Loading States** - Visual feedback during processing  

### API Endpoints

The backend provides these REST API endpoints:

#### `GET /health`
Check if the API server is running and the model is loaded.

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "model_name": "Random Forest"
}
```

#### `POST /predict`
Classify a single URL.

**Request:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "success": true,
  "url": "https://example.com",
  "prediction": "Benign",
  "label": 0,
  "probability_benign": 0.95,
  "probability_malicious": 0.05,
  "confidence": 0.95
}
```

#### `POST /predict/batch`
Classify multiple URLs at once.

**Request:**
```json
{
  "urls": [
    "https://example.com",
    "https://suspicious-site.tk"
  ]
}
```

### Troubleshooting

#### "Cannot connect to API server"
- Make sure the backend server is running (`python api/app.py`)
- Check that it's running on `http://localhost:5000`
- Verify no firewall is blocking the connection

#### "Model not loaded"
- Run `python train.py` first to create the model
- Verify `models/best_model.pkl` exists
- Check the backend server logs for error messages

#### CORS Errors
- The backend already has CORS enabled
- If you see CORS errors, make sure you're accessing the frontend via `http://localhost` or `file://` protocol

#### Port Already in Use
- If port 5000 is busy, you can change it in `api/app.py`:
  ```python
  app.run(host='0.0.0.0', port=5001)  # Change port number
  ```
- Then update `API_BASE_URL` in `frontend/script.js` to match

### Project Structure

```
IS/
├── api/
│   └── app.py              # Flask backend server
├── frontend/
│   ├── index.html          # Main HTML file
│   ├── styles.css          # Styling with themes
│   └── script.js           # Frontend JavaScript
├── models/
│   └── best_model.pkl      # Trained ML model (created after training)
├── url_classifier/         # Core ML modules
└── requirements.txt        # Python dependencies
```

### Next Steps

- **Production Deployment**: For production, consider using:
  - Gunicorn or uWSGI for the Flask server
  - Nginx as a reverse proxy
  - HTTPS/SSL certificates
  - Environment variables for configuration

- **Enhancements**: The codebase is ready for:
  - User authentication
  - Database integration
  - Advanced analytics
  - API rate limiting
  - Caching mechanisms

---

**Enjoy your URL Phishing Detection Web Application! 🛡️**

