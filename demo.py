"""
Demo Script
Demonstrates the URL classification system with example URLs.
"""

import sys
import os
from pathlib import Path

# Add project root to Python path to fix ModuleNotFoundError
project_root = Path(__file__).parent.absolute()
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

try:
    from url_classifier.url_classifier import URLClassifier
except ImportError as e:
    print("="*80)
    print("IMPORT ERROR")
    print("="*80)
    print(f"Error: {e}")
    print("\nTroubleshooting:")
    print("1. Make sure you're running this script from the project root folder")
    print("   (the folder containing 'url_classifier' and 'demo.py')")
    print("2. Current working directory:", os.getcwd())
    print("3. Project root should be:", project_root)
    print("4. Try running: cd <project_root> && python demo.py")
    print("="*80)
    sys.exit(1)


def main():
    """Run demonstration of URL classification."""
    print("="*80)
    print("URL Phishing Detection System - Demonstration")
    print("="*80)
    
    # Check if model exists
    model_path = 'models/best_model.pkl'
    if not Path(model_path).exists():
        print(f"\nModel not found at {model_path}")
        print("Please train a model first by running: python train.py")
        return
    
    # Load classifier
    try:
        classifier = URLClassifier(model_path)
        print(f"\nModel loaded: {classifier.model_name}")
    except Exception as e:
        print(f"Error loading model: {e}")
        return
    
    # Example URLs to test
    test_urls = [
        # Benign URLs
        "https://www.google.com",
        "https://www.github.com",
        "https://www.wikipedia.org",
        "https://www.microsoft.com/en-us",
        
        # Potentially malicious URLs (patterns)
        "http://verify-account-secure.tk/login",
        "https://secure-login-update.ml/verify",
        "http://192.168.1.1/login.php",
        "https://bank-verify-urgent.cf/update",
        "http://suspicious-site.tk/secure-login",
    ]
    
    print("\n" + "="*80)
    print("Classifying Example URLs")
    print("="*80)
    
    results = []
    for url in test_urls:
        try:
            result = classifier.classify(url)
            results.append(result)
            
            # Display result
            print(f"\nURL: {result['url']}")
            print(f"Prediction: {result['prediction']}")
            if result.get('probability_malicious') is not None:
                print(f"  Malicious Probability: {result['probability_malicious']:.2%}")
                print(f"  Benign Probability: {result['probability_benign']:.2%}")
                print(f"  Confidence: {result['confidence']:.2%}")
            print("-" * 80)
            
        except Exception as e:
            print(f"\nError classifying {url}: {e}")
    
    # Summary
    print("\n" + "="*80)
    print("Summary")
    print("="*80)
    benign_count = sum(1 for r in results if r['prediction'] == 'Benign')
    malicious_count = sum(1 for r in results if r['prediction'] == 'Malicious')
    print(f"Total URLs tested: {len(results)}")
    print(f"Benign: {benign_count}")
    print(f"Malicious: {malicious_count}")
    print("="*80)


if __name__ == '__main__':
    main()

