# 🚀 Quick Start Guide - Web Application

## Prerequisites Check

Before starting, ensure you have:
- ✅ Python 3.8+ installed
- ✅ Virtual environment activated (optional but recommended)
- ✅ All dependencies installed: `pip install -r requirements.txt`
- ✅ Trained model at `models/best_model.pkl` (if not, see Step 0)

---

## Step 0: Train Model (If Not Already Done)

If you don't have a trained model yet:

```bash
python train.py
```

This will:
- Load the dataset from `data/dataset.csv`
- Train 4 ML models
- Save the best model to `models/best_model.pkl`
- Generate evaluation results

**Time required:** 2-5 minutes (depending on dataset size)

---

## Step 1: Start the Backend API

**Option A: Using the start script (Recommended)**
```bash
python start_web_app.py
```

**Option B: Direct Flask command**
```bash
python api/app.py
```

You should see:
```
============================================================
URL Phishing Detection API Server
============================================================
Loading model from models/best_model.pkl...
Model loaded successfully: [Model Name]
Starting Flask server...
API will be available at: http://localhost:5000
============================================================
```

**Keep this terminal window open!** The server must be running for the frontend to work.

---

## Step 2: Open the Frontend

### Method 1: Direct File Open (Simplest)
1. Navigate to the `frontend` folder
2. Double-click `index.html`
3. Your default browser will open the application

### Method 2: Local Server (Recommended for Development)
```bash
# In a new terminal window
cd frontend
python -m http.server 8000
```

Then open: `http://localhost:8000`

---

## Step 3: Use the Application

1. **Enter a URL** in the input box (e.g., `https://example.com`)
2. **Click "Check Safety"** button
3. **View Results:**
   - Prediction (Benign/Malicious)
   - Confidence score
   - Probability breakdown
4. **Check History** - Recent checks are saved automatically
5. **Toggle Theme** - Click the moon/sun icon for dark/light mode

---

## 🎯 Testing the API

### Test Health Endpoint
```bash
curl http://localhost:5000/health
```

### Test Classification
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"https://example.com\"}"
```

---

## 🐛 Troubleshooting

### "Cannot connect to API server"
- ✅ Make sure backend is running (`python api/app.py`)
- ✅ Check that port 5000 is not in use
- ✅ Verify no firewall is blocking the connection

### "Model not loaded"
- ✅ Run `python train.py` to create the model
- ✅ Verify `models/best_model.pkl` exists
- ✅ Check backend terminal for error messages

### CORS Errors
- ✅ Ensure `flask-cors` is installed: `pip install flask-cors`
- ✅ Check that frontend is using correct API URL

### Port Already in Use
If port 5000 is busy, edit `api/app.py` and change:
```python
app.run(port=5000)  # Change to another port, e.g., 5001
```
Then update `frontend/script.js`:
```javascript
const API_BASE_URL = 'http://localhost:5001';  // Match the port
```

---

## 📁 File Structure

```
IS/
├── api/
│   └── app.py              ← Backend API server
├── frontend/
│   ├── index.html          ← Main HTML file
│   ├── styles.css          ← Styling
│   └── script.js           ← Frontend logic
├── models/
│   └── best_model.pkl      ← Trained model (create with train.py)
├── start_web_app.py        ← Quick start script
└── requirements.txt        ← Dependencies
```

---

## 🎨 Features

- ✅ **Modern UI** - Beautiful, responsive design
- ✅ **Dark/Light Theme** - Toggle with one click
- ✅ **Real-time Results** - Instant classification
- ✅ **History Tracking** - Browser-based storage
- ✅ **Error Handling** - User-friendly messages
- ✅ **Mobile Friendly** - Works on all devices

---

## 🚀 Next Steps

1. **Customize the UI** - Edit `frontend/styles.css`
2. **Add Features** - Extend `frontend/script.js`
3. **Deploy** - See `WEB_APP_README.md` for production deployment

---

**Need Help?** Check `WEB_APP_README.md` for detailed documentation.

