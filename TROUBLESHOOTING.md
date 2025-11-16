# Troubleshooting Guide

This guide helps you resolve common issues when running the URL Phishing Detection System.

## Common Issues & Fixes

### 1. ModuleNotFoundError: No module named 'url_classifier'

**Error Message:**
```
ModuleNotFoundError: No module named 'url_classifier'
```

**Causes:**
- Running the script from the wrong directory
- Python can't find the `url_classifier` package

**Solutions:**

1. **Check your current directory:**
   ```bash
   # Windows
   cd
   
   # Linux/Mac
   pwd
   ```

2. **Navigate to the project root:**
   ```bash
   # The project root should contain:
   # - url_classifier/ (folder)
   # - train.py
   # - demo.py
   # - requirements.txt
   
   cd C:\Users\Hp\Desktop\IS  # Windows example
   # or
   cd ~/Desktop/IS  # Linux/Mac example
   ```

3. **Run the script from the project root:**
   ```bash
   python train.py
   # or
   python demo.py
   # or
   python -m url_classifier.cli
   ```

4. **Verify the project structure:**
   ```
   IS/
   ├── url_classifier/
   │   ├── __init__.py
   │   ├── cli.py
   │   ├── data_processor.py
   │   ├── feature_extractor.py
   │   ├── model_trainer.py
   │   └── url_classifier.py
   ├── train.py
   ├── demo.py
   └── requirements.txt
   ```

---

### 2. FileNotFoundError: dataset.csv

**Error Message:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'data/dataset.csv'
```

**Causes:**
- Dataset file doesn't exist
- Wrong file path
- File in different location

**Solutions:**

1. **Check if the data folder exists:**
   ```bash
   # Windows
   dir data
   
   # Linux/Mac
   ls data
   ```

2. **Verify the dataset file location:**
   - The file should be at: `data/dataset.csv` or `data/url_dataset.csv`
   - Make sure you're in the project root when running scripts

3. **Create the data folder if it doesn't exist:**
   ```bash
   # Windows
   mkdir data
   
   # Linux/Mac
   mkdir -p data
   ```

4. **The script will auto-create a sample dataset if none is found:**
   - If you see "Creating sample dataset for demonstration...", the script is creating one for you
   - For production use, replace it with a real dataset

5. **Dataset format requirements:**
   - CSV file with at least two columns:
     - `url` (or `URL`): The URL string
     - `label` (or `type`): Classification (0/benign or 1/malicious)
   - Example:
     ```csv
     url,type
     https://www.google.com,benign
     http://suspicious-site.tk/login,phishing
     ```

---

### 3. ImportError: cannot import name

**Error Message:**
```
ImportError: cannot import name 'URLClassifier' from 'url_classifier'
```

**Causes:**
- Missing `__init__.py` file
- Corrupted package structure
- Python cache issues

**Solutions:**

1. **Verify `__init__.py` exists:**
   ```bash
   # Check if the file exists
   # Windows
   dir url_classifier\__init__.py
   
   # Linux/Mac
   ls url_classifier/__init__.py
   ```

2. **Clear Python cache:**
   ```bash
   # Remove __pycache__ folders
   # Windows
   rmdir /s /q url_classifier\__pycache__
   
   # Linux/Mac
   rm -rf url_classifier/__pycache__
   ```

3. **Reinstall the package (if installed):**
   ```bash
   pip uninstall url-classifier
   pip install -e .
   ```

4. **Check `__init__.py` content:**
   - The file can be empty or contain package metadata
   - It just needs to exist to mark the folder as a Python package

---

### 4. PermissionError on Windows

**Error Message:**
```
PermissionError: [Errno 13] Permission denied: 'data/dataset.csv'
```

**Causes:**
- File is open in another program (Excel, Notepad, etc.)
- Insufficient permissions
- Antivirus blocking access

**Solutions:**

1. **Close programs using the file:**
   - Close Excel, Notepad, or any editor with the file open
   - Check Task Manager for processes using the file

2. **Run as Administrator:**
   ```bash
   # Right-click Command Prompt or PowerShell
   # Select "Run as Administrator"
   # Then navigate to project and run:
   cd C:\Users\Hp\Desktop\IS
   python train.py
   ```

3. **Check file/folder permissions:**
   - Right-click the `data` folder
   - Properties → Security
   - Ensure your user has "Full control" or at least "Write" permissions

4. **Disable antivirus temporarily:**
   - Some antivirus software blocks file operations
   - Add the project folder to antivirus exclusions

5. **Use a different location:**
   - Try running from a user folder (Desktop, Documents)
   - Avoid system-protected folders (Program Files, etc.)

---

### 5. Additional Common Issues

#### Issue: "No module named 'tqdm'"
**Fix:**
```bash
pip install -r requirements.txt
```

#### Issue: "No module named 'sklearn'"
**Fix:**
```bash
pip install scikit-learn
```

#### Issue: Model file not found
**Error:** `Model not found at models/best_model.pkl`

**Fix:**
1. Train a model first: `python train.py`
2. Check if `models/` folder exists
3. Verify the model was saved successfully

#### Issue: Unicode/Encoding errors on Windows
**Error:** `UnicodeEncodeError: 'charmap' codec can't encode character`

**Fix:**
- The code has been updated to use ASCII-safe characters
- If you still see this, set environment variable:
  ```bash
  set PYTHONIOENCODING=utf-8
  ```

#### Issue: Out of memory during training
**Error:** `MemoryError` or system becomes slow

**Fix:**
1. Use a smaller dataset sample:
   ```python
   # In train.py, limit the dataset size
   df = df.head(50000)  # Use first 50k rows
   ```
2. Close other applications
3. Increase virtual memory (Windows) or swap space (Linux)

---

## Getting Help

If you continue to experience issues:

1. **Check the error message carefully** - it usually indicates what's wrong
2. **Verify your Python version:** `python --version` (should be 3.8+)
3. **Verify all dependencies are installed:** `pip list`
4. **Check the project structure** matches the expected layout
5. **Review the README.md** for setup instructions

## Quick Verification Checklist

Before running the project, verify:

- [ ] Python 3.8+ is installed
- [ ] All dependencies installed: `pip install -r requirements.txt`
- [ ] You're in the project root directory
- [ ] `url_classifier/` folder exists with `__init__.py`
- [ ] `data/` folder exists (will be created automatically if missing)
- [ ] Dataset file is in `data/` folder (or sample will be created)
- [ ] No permission errors on Windows (run as Admin if needed)

---

**Note:** The scripts have been updated to automatically handle many of these issues with better error messages and path resolution.

