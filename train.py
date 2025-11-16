"""
Training Script
Main script for training the URL classification model.
"""

import sys
import os
import pandas as pd
from pathlib import Path

# Add project root to Python path to fix ModuleNotFoundError
project_root = Path(__file__).parent.absolute()
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

try:
    from url_classifier.data_processor import DataProcessor
    from url_classifier.model_trainer import ModelTrainer
except ImportError as e:
    print("="*80)
    print("IMPORT ERROR")
    print("="*80)
    print(f"Error: {e}")
    print("\nTroubleshooting:")
    print("1. Make sure you're running this script from the project root folder")
    print("   (the folder containing 'url_classifier' and 'train.py')")
    print("2. Current working directory:", os.getcwd())
    print("3. Project root should be:", project_root)
    print("4. Try running: cd <project_root> && python train.py")
    print("="*80)
    sys.exit(1)


def main():
    """Main training function."""
    print("="*80)
    print("URL Phishing Detection System - Model Training")
    print("="*80)
    
    # Check if dataset file exists
    data_file = 'data/dataset.csv'
    data_file_path = Path(data_file)
    
    if not data_file_path.exists():
        # Try alternative path
        alt_data_file = 'data/url_dataset.csv'
        alt_data_file_path = Path(alt_data_file)
        if alt_data_file_path.exists():
            data_file = alt_data_file
            data_file_path = alt_data_file_path
        else:
            print("\n" + "="*80)
            print("DATASET FILE NOT FOUND")
            print("="*80)
            print(f"Looking for dataset at: {data_file_path.absolute()}")
            print(f"Alternative path checked: {alt_data_file_path.absolute()}")
            print("\nTroubleshooting:")
            print("1. Make sure your dataset CSV file is in the 'data' folder")
            print("2. The file should be named 'dataset.csv' or 'url_dataset.csv'")
            print("3. Required columns: 'url' (or 'URL') and 'type' (or 'label')")
            print("\nCreating sample dataset for demonstration...")
            print("="*80)
            
            # Create data directory if it doesn't exist
            data_file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Create sample dataset
            try:
                processor = DataProcessor()
                processor.create_sample_dataset(str(data_file_path), num_samples=2000)
                print(f"\nSample dataset created at: {data_file_path.absolute()}")
                print("\nNote: For better results, replace this with a real dataset from:")
                print("  - Kaggle: https://www.kaggle.com/datasets")
                print("  - PhishTank: https://www.phishtank.com/")
                print("  - UCI ML Repository")
            except PermissionError as pe:
                print("\n" + "="*80)
                print("PERMISSION ERROR")
                print("="*80)
                print(f"Error: {pe}")
                print("\nTroubleshooting:")
                print("1. On Windows: Try running as Administrator")
                print("2. Close any programs that might be using the file")
                print("3. Check folder permissions for the 'data' directory")
                print("4. Try creating the 'data' folder manually first")
                print("="*80)
                sys.exit(1)
    
    try:
        # Load and process data
        processor = DataProcessor()
        print(f"\nLoading data from {data_file}...")
        
        # Check if file exists and is readable
        if not Path(data_file).exists():
            raise FileNotFoundError(f"Dataset file not found: {Path(data_file).absolute()}")
        
        # Check which label column exists
        try:
            sample_df = pd.read_csv(data_file, nrows=1)
        except PermissionError as pe:
            print("\n" + "="*80)
            print("PERMISSION ERROR")
            print("="*80)
            print(f"Error: Cannot read dataset file - {pe}")
            print("\nTroubleshooting:")
            print("1. On Windows: Try running as Administrator")
            print("2. Close Excel or any program that might have the file open")
            print("3. Check file permissions")
            print("="*80)
            sys.exit(1)
        except Exception as e:
            print(f"\nError reading dataset file: {e}")
            print(f"File path: {Path(data_file).absolute()}")
            sys.exit(1)
        
        label_col = 'type' if 'type' in sample_df.columns else 'label'
        url_col = 'url' if 'url' in sample_df.columns else 'URL'
        
        if label_col not in sample_df.columns and 'label' not in sample_df.columns:
            print("\n" + "="*80)
            print("DATASET FORMAT ERROR")
            print("="*80)
            print(f"Error: Dataset must have a 'label' or 'type' column")
            print(f"Found columns: {list(sample_df.columns)}")
            print("\nRequired columns:")
            print("  - 'url' (or 'URL'): The URL string")
            print("  - 'label' (or 'type'): The classification (0/benign or 1/malicious)")
            print("="*80)
            sys.exit(1)
        
        if url_col not in sample_df.columns and 'url' not in sample_df.columns:
            print("\n" + "="*80)
            print("DATASET FORMAT ERROR")
            print("="*80)
            print(f"Error: Dataset must have a 'url' or 'URL' column")
            print(f"Found columns: {list(sample_df.columns)}")
            print("="*80)
            sys.exit(1)
        
        df = processor.load_data(data_file, label_column=label_col, url_column=url_col)
        print(f"Loaded {len(df)} URLs")
        print(f"  Benign: {len(df[df[label_col] == 0])}")
        print(f"  Malicious: {len(df[df[label_col] == 1])}")
        
        # Extract features
        print("\nExtracting features from URLs...")
        features, labels = processor.prepare_training_data(df, url_column=url_col, label_column=label_col)
        print(f"Extracted {len(features.columns)} features from {len(features)} URLs")
        
        # Train models
        trainer = ModelTrainer()
        X_train, X_test, y_train, y_test = trainer.prepare_data(features, labels)
        
        print(f"\nTraining set: {len(X_train)} samples")
        print(f"Test set: {len(X_test)} samples")
        
        trainer.train_models(X_train, y_train)
        
        # Evaluate models
        trainer.evaluate_models(X_test, y_test)
        trainer.print_evaluation_summary()
        
        # Select and save best model
        trainer.select_best_model()
        trainer.save_best_model()
        trainer.save_evaluation_results()
        
        print("\n" + "="*80)
        print("Training completed successfully!")
        print("="*80)
        print(f"\nModel saved to: models/best_model.pkl")
        print(f"Evaluation results saved to: results/evaluation_results.json")
        print("\nYou can now use the classifier with:")
        print("  python -m url_classifier.cli")
        print("  or")
        print("  python -m url_classifier.cli classify <URL>")
        
    except Exception as e:
        print(f"\nError during training: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

