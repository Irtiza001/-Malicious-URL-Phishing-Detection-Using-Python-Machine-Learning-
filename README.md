# URL Phishing Detection System

A Python-based machine learning system for detecting malicious and phishing URLs. This system uses various machine learning algorithms to classify URLs as either 'Benign' or 'Malicious/Phishing' based on extracted features.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dataset Description](#dataset-description)
- [Feature Engineering](#feature-engineering)
- [Model Training](#model-training)
- [Model Evaluation](#model-evaluation)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

### Motivation and Objectives

Phishing attacks are one of the most common cybersecurity threats, with attackers using deceptive URLs to trick users into revealing sensitive information. This project aims to develop an automated system that can identify potentially malicious URLs before users interact with them.

**Objectives:**
- Develop a robust machine learning-based URL classification system
- Extract meaningful features from URLs that indicate malicious intent
- Train and evaluate multiple classification models
- Provide an easy-to-use interface for URL classification
- Achieve high accuracy in distinguishing between benign and malicious URLs

## Features

- **Comprehensive Feature Extraction**: Extracts 25+ features from URLs including length, special characters, domain information, suspicious tokens, and more
- **Multiple ML Models**: Supports Logistic Regression, Random Forest, Support Vector Machine, and Neural Networks
- **Model Evaluation**: Comprehensive evaluation using Accuracy, Precision, Recall, F1-Score, and ROC-AUC metrics
- **CLI Interface**: Easy-to-use command-line interface for URL classification
- **Batch Processing**: Classify multiple URLs from a file
- **Probability Scores**: Provides confidence scores and probability of maliciousness
- **Modular Design**: Well-structured, modular codebase for easy extension

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone or Download the Project

```bash
cd IS
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Verify Installation

```bash
python -c "import url_classifier; print('Installation successful!')"
```

## Quick Start

### 1. Train a Model

First, you need to train a model. The system will create a sample dataset if none is provided:

```bash
python train.py
```

Or train with your own dataset:

```bash
python -m url_classifier.cli train your_dataset.csv --url-column url --label-column label
```

### 2. Classify URLs

**Interactive Mode:**
```bash
python -m url_classifier.cli
```

**Single URL:**
```bash
python -m url_classifier.cli classify "https://example.com"
```

**Batch Classification:**
```bash
python -m url_classifier.cli batch urls.txt -o results.csv
```

**Run Demo:**
```bash
python demo.py
```

## Usage

### Training a Model

The training script will:
1. Load and preprocess the dataset
2. Extract features from all URLs
3. Train multiple ML models
4. Evaluate and compare models
5. Save the best model

```bash
python train.py
```

**Dataset Format:**
Your CSV file should have at least two columns:
- `url`: The URL string
- `label`: The label (0/benign or 1/malicious)

Example:
```csv
url,label
https://www.google.com,0
http://verify-account.tk/login,1
```

### Classifying URLs

#### Interactive Mode

```bash
python -m url_classifier.cli
```

Enter URLs one by one. Type 'quit' or 'exit' to stop.

#### Command Line

```bash
# Single URL
python -m url_classifier.cli classify "https://suspicious-site.tk/login"

# Batch processing
python -m url_classifier.cli batch input_urls.txt -o output_results.csv
```

#### Python API

```python
from url_classifier.url_classifier import URLClassifier

# Load classifier
classifier = URLClassifier('models/best_model.pkl')

# Classify a URL
result = classifier.classify("https://example.com")
print(f"Prediction: {result['prediction']}")
print(f"Probability: {result['probability_malicious']:.2%}")
```

## Project Structure

```
IS/
├── url_classifier/          # Main package
│   ├── __init__.py
│   ├── feature_extractor.py # URL feature extraction
│   ├── data_processor.py    # Data loading and preprocessing
│   ├── model_trainer.py     # Model training and evaluation
│   ├── url_classifier.py    # URL classification interface
│   └── cli.py              # Command-line interface
├── data/                    # Dataset directory
│   └── url_dataset.csv     # Training dataset
├── models/                  # Saved models
│   └── best_model.pkl      # Best trained model
├── results/                 # Evaluation results
│   └── evaluation_results.json
├── train.py                # Training script
├── demo.py                 # Demonstration script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Dataset Description

### Data Sources

The system can work with datasets from various sources:

1. **Kaggle**: Multiple URL classification datasets available
2. **PhishTank**: Public database of phishing URLs
3. **UCI ML Repository**: Various cybersecurity datasets
4. **Custom Datasets**: Your own labeled URL data

### Dataset Requirements

- **Format**: CSV file
- **Required Columns**: 
  - URL column (default: `url`)
  - Label column (default: `label`)
- **Labels**: 
  - Benign: `0`, `benign`, `good`, `legitimate`, `safe`
  - Malicious: `1`, `malicious`, `phishing`, `bad`, `unsafe`

### Sample Dataset

If no dataset is provided, the system will generate a sample dataset for demonstration purposes. For production use, replace this with a real, comprehensive dataset.

## Feature Engineering

The system extracts 25 features from each URL:

### Basic URL Features
1. **URL Length**: Total character count
2. **Domain Length**: Length of the domain name
3. **Path Length**: Length of the URL path
4. **Query Length**: Length of query parameters

### Character Analysis
5. **Number of Special Characters**: Count of non-alphanumeric characters
6. **Special Character Ratio**: Proportion of special characters
7. **Number of Dots**: Count of periods
8. **Number of Hyphens**: Count in domain
9. **Number of Slashes**: Count of forward slashes
10. **Number of Equals Signs**: Common in phishing URLs
11. **Number of Question Marks**: Query parameter indicators
12. **Number of Ampersands**: Multiple parameters
13. **Number of Percent Signs**: URL encoding indicators
14. **Digit Ratio**: Proportion of numeric characters

### Security Indicators
15. **Uses HTTPS**: Whether URL uses secure protocol
16. **Has IP Address**: Presence of IP instead of domain
17. **Has Port Number**: Non-standard port usage
18. **Has @ Symbol**: Often used in phishing URLs

### Domain Analysis
19. **Number of Subdomains**: Count of subdomain levels
20. **Subdomain Length**: Length of subdomain portion
21. **Suspicious TLD**: Presence of suspicious top-level domains (.tk, .ml, .ga, etc.)

### Content Analysis
22. **Number of Suspicious Tokens**: Count of phishing-related keywords
23. **Number of Redirects**: Presence of redirect patterns (../, ./)
24. **Is Short URL**: Detection of URL shortening services
25. **URL Entropy**: Shannon entropy (randomness indicator)

### Feature Extraction Example

```python
from url_classifier.feature_extractor import URLFeatureExtractor

extractor = URLFeatureExtractor()
features = extractor.extract_features("https://verify-account.tk/login")
print(features)
```

## Model Training

### Supported Models

1. **Logistic Regression**: Fast, interpretable baseline model
2. **Random Forest**: Ensemble method with good performance
3. **Support Vector Machine**: Effective for binary classification
4. **Neural Network**: Multi-layer perceptron for complex patterns

### Training Process

1. **Data Splitting**: 80% training, 20% testing (stratified)
2. **Feature Scaling**: StandardScaler for normalization
3. **Model Training**: All models trained on the same data
4. **Evaluation**: Comprehensive metrics on test set
5. **Model Selection**: Best model selected based on F1-score

### Training Output

The training process generates:
- Trained models for each algorithm
- Best model saved to `models/best_model.pkl`
- Evaluation results saved to `results/evaluation_results.json`
- Console output with detailed metrics

## Model Evaluation

### Evaluation Metrics

The system evaluates models using:

1. **Accuracy**: Overall correctness
2. **Precision**: True positives / (True positives + False positives)
3. **Recall**: True positives / (True positives + False negatives)
4. **F1-Score**: Harmonic mean of precision and recall
5. **ROC-AUC**: Area under the ROC curve

### Example Evaluation Results

```
MODEL EVALUATION SUMMARY
================================================================================
Model                    Accuracy  Precision  Recall   F1-Score  ROC-AUC
Logistic Regression      0.9234    0.9156    0.9321   0.9238    0.9789
Random Forest            0.9456    0.9412    0.9501   0.9456    0.9892
Support Vector Machine   0.9389    0.9345    0.9432   0.9388    0.9856
Neural Network           0.9423    0.9398    0.9445   0.9421    0.9878
================================================================================
```

## Troubleshooting

If you encounter issues while running the project, please refer to the comprehensive [TROUBLESHOOTING.md](TROUBLESHOOTING.md) guide.

### Common Issues Quick Fix

1. **ModuleNotFoundError: No module named 'url_classifier'**
   - Make sure you're running scripts from the project root folder
   - The scripts now automatically add the project root to Python path

2. **FileNotFoundError: dataset.csv**
   - Place your dataset in `data/dataset.csv` or `data/url_dataset.csv`
   - The script will create a sample dataset if none is found

3. **ImportError: cannot import name**
   - Verify `url_classifier/__init__.py` exists (it can be empty)
   - Clear Python cache: `rm -rf url_classifier/__pycache__` (Linux/Mac) or delete `__pycache__` folder (Windows)

4. **PermissionError on Windows**
   - Run Command Prompt or PowerShell as Administrator
   - Close any programs that might have files open (Excel, etc.)

For detailed solutions, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Limitations

1. **Dataset Dependency**: Model performance heavily depends on training data quality and diversity
2. **Feature-Based Only**: Does not analyze actual webpage content or behavior
3. **Static Analysis**: Cannot detect dynamic or context-based attacks
4. **False Positives**: Legitimate URLs with unusual patterns may be flagged
5. **Evolving Threats**: New attack patterns may not be detected without retraining
6. **No Real-Time Updates**: Requires manual retraining to adapt to new threats

## Future Improvements

### Short-term Enhancements
- [ ] Web-based GUI interface
- [ ] Real-time URL checking via API
- [ ] Integration with threat intelligence feeds
- [ ] Model retraining pipeline
- [ ] Confidence threshold configuration

### Advanced Features
- [ ] Deep learning models (LSTM, CNN)
- [ ] Content-based analysis (webpage scraping)
- [ ] DNS and WHOIS data integration
- [ ] Domain age and reputation checking
- [ ] Ensemble methods with voting
- [ ] Explainable AI (feature importance visualization)

### Performance Optimizations
- [ ] Model quantization for faster inference
- [ ] Batch processing optimization
- [ ] Caching mechanisms
- [ ] Distributed training support

### Data Improvements
- [ ] Automatic dataset collection from multiple sources
- [ ] Data augmentation techniques
- [ ] Handling imbalanced datasets
- [ ] Active learning for model improvement

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Datasets from Kaggle, PhishTank, and UCI ML Repository
- scikit-learn for machine learning algorithms
- tldextract for domain parsing

## Contact

For questions or issues, please open an issue on the repository.

---

**Note**: This system is for educational and research purposes. Always use multiple security layers and keep your models updated with the latest threat intelligence for production use.

