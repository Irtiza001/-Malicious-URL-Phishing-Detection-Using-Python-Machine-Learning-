# Quick Start Guide

This guide will help you get started with the URL Phishing Detection System in minutes.

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Train Your First Model

The system will automatically create a sample dataset if you don't have one:

```bash
python train.py
```

This will:
- Create a sample dataset (if needed)
- Extract features from URLs
- Train 4 different ML models
- Evaluate and select the best model
- Save the model to `models/best_model.pkl`

**Expected time**: 2-5 minutes depending on your system

## Step 3: Test the System

### Option A: Run the Demo

```bash
python demo.py
```

This will classify several example URLs and show the results.

### Option B: Interactive Mode

```bash
python -m url_classifier.cli
```

Then enter URLs one by one. Type 'quit' to exit.

### Option C: Classify a Single URL

```bash
python -m url_classifier.cli classify "https://example.com"
```

### Option D: Batch Classification

Create a file `urls.txt` with one URL per line:
```
https://www.google.com
https://www.github.com
http://suspicious-site.tk/login
```

Then run:
```bash
python -m url_classifier.cli batch urls.txt -o results.csv
```

## Step 4: Use Your Own Dataset (Optional)

To train with your own dataset:

1. Prepare a CSV file with columns:
   - `url`: The URL string
   - `label`: 0 for benign, 1 for malicious

2. Train with your dataset:
```bash
python -m url_classifier.cli train your_dataset.csv --url-column url --label-column label
```

## Using the Python API

```python
from url_classifier.url_classifier import URLClassifier

# Load the trained model
classifier = URLClassifier('models/best_model.pkl')

# Classify a URL
result = classifier.classify("https://example.com")

print(f"URL: {result['url']}")
print(f"Prediction: {result['prediction']}")
print(f"Malicious Probability: {result['probability_malicious']:.2%}")
print(f"Confidence: {result['confidence']:.2%}")
```

## Troubleshooting

### "Model not found" error
- Make sure you've run `python train.py` first
- Check that `models/best_model.pkl` exists

### "Dataset not found" error
- The system will create a sample dataset automatically
- Or provide your own dataset using the `train` command

### Import errors
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Verify you're using Python 3.8 or higher

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Explore the code in the `url_classifier/` directory
- Customize features in `url_classifier/feature_extractor.py`
- Experiment with different models in `url_classifier/model_trainer.py`

## Getting Help

If you encounter issues:
1. Check the error message carefully
2. Verify all dependencies are installed
3. Ensure you've trained a model before classifying URLs
4. Check the README.md for detailed documentation

Happy classifying! 🚀

