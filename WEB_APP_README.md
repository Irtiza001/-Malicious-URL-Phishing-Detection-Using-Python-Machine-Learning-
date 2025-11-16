# URL Phishing Detection System - Web Application

A modern, responsive web application for the URL Phishing Detection System with a beautiful UI and RESTful API backend.

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Trained model file at `models/best_model.pkl` (run `python train.py` first if not available)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Step 1: Install Dependencies

```bash
# Activate virtual environment (if using one)
.\venv\Scripts\Activate.ps1  # Windows PowerShell
# or
source venv/bin/activate     # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Start the Backend API Server

```bash
python api/app.py
```

The API server will start on `http://localhost:5000`

You should see:
```
============================================================
URL Phishing Detection API Server
============================================================
Loading model from models/best_model.pkl...
Model loaded successfully: [Model Name]
Starting Flask server...
API will be available at: http://localhost:5000
Endpoints:
  GET  /health  - Health check
  POST /predict - Classify a single URL
  POST /predict/batch - Classify multiple URLs
============================================================
```

### Step 3: Open the Frontend

Simply open `frontend/index.html` in your web browser:

**Option 1: Double-click**
- Navigate to the `frontend` folder
- Double-click `index.html`

**Option 2: Open via browser**
- Right-click `frontend/index.html`
- Select "Open with" → Choose your browser

**Option 3: Use a local server (recommended for development)**
```bash
# Python 3
cd frontend
python -m http.server 8000

# Then open: http://localhost:8000
```

## 📁 Project Structure

```
IS/
├── api/
│   └── app.py              # Flask backend API server
├── frontend/
│   ├── index.html          # Main HTML file
│   ├── styles.css          # Styling and themes
│   └── script.js           # Frontend JavaScript logic
├── models/
│   └── best_model.pkl      # Trained ML model (created after training)
├── url_classifier/         # Core ML package
└── requirements.txt        # Python dependencies
```

## 🎯 Features

### Backend API

- **POST /predict** - Classify a single URL
  ```json
  Request: { "url": "https://example.com" }
  Response: {
    "success": true,
    "prediction": "Benign",
    "confidence": 0.95,
    "probability_benign": 0.95,
    "probability_malicious": 0.05
  }
  ```

- **POST /predict/batch** - Classify multiple URLs
  ```json
  Request: { "urls": ["https://example.com", "https://suspicious.tk"] }
  ```

- **GET /health** - Check API health and model status

### Frontend Features

- ✅ **Modern, Responsive UI** - Works on desktop, tablet, and mobile
- ✅ **Dark/Light Theme** - Toggle between themes with one click
- ✅ **Real-time Classification** - Instant results with loading animations
- ✅ **History Tracking** - Stores recent checks in browser localStorage
- ✅ **Error Handling** - User-friendly error messages
- ✅ **URL Validation** - Automatic URL format validation
- ✅ **Confidence Visualization** - Visual progress bars and probability scores
- ✅ **No Page Reloads** - Smooth, dynamic updates

## 🎨 UI Screenshots

### Light Theme
- Clean, modern interface with gradient accents
- Professional color scheme
- Easy-to-read typography

### Dark Theme
- Eye-friendly dark mode
- Reduced eye strain
- Perfect for low-light environments

## 🔧 Configuration

### Change API URL

If your backend runs on a different port or host, edit `frontend/script.js`:

```javascript
const API_BASE_URL = 'http://localhost:5000';  // Change this
```

### Adjust History Limit

Edit `frontend/script.js`:

```javascript
const MAX_HISTORY_ITEMS = 50;  // Change this
```

## 🐛 Troubleshooting

### "Cannot connect to API server"

1. Make sure the backend is running: `python api/app.py`
2. Check that the server is on `http://localhost:5000`
3. Verify no firewall is blocking the connection
4. Check browser console for detailed error messages

### "Model not loaded" error

1. Ensure you've trained a model: `python train.py`
2. Verify `models/best_model.pkl` exists
3. Check backend logs for loading errors

### CORS Errors

The backend includes `flask-cors` to handle CORS. If you still see errors:
- Make sure `flask-cors` is installed: `pip install flask-cors`
- Check that the frontend is accessing the correct API URL

### History not saving

- Check browser localStorage is enabled
- Clear browser cache and try again
- Check browser console for errors

## 📝 API Usage Examples

### Using cURL

```bash
# Health check
curl http://localhost:5000/health

# Classify URL
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

### Using Python

```python
import requests

# Classify URL
response = requests.post(
    'http://localhost:5000/predict',
    json={'url': 'https://example.com'}
)
result = response.json()
print(result)
```

### Using JavaScript (fetch)

```javascript
const response = await fetch('http://localhost:5000/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url: 'https://example.com' })
});
const result = await response.json();
console.log(result);
```

## 🚀 Production Deployment

### Backend Deployment

For production, use a production WSGI server:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 api.app:app
```

### Frontend Deployment

1. Deploy `frontend/` folder to any static hosting (Netlify, Vercel, GitHub Pages)
2. Update `API_BASE_URL` in `script.js` to point to your production API
3. Ensure CORS is properly configured on the backend

## 📄 License

Same as the main project (MIT License)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Note**: This web application is built on top of the existing URL Phishing Detection System. Make sure you've trained a model before using the web interface.

