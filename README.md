# Credit Card Fraud Detection

This project aims to detect fraudulent credit card transactions using machine learning models. The application is built with a Flask web framework, and the model training and evaluation are done using various machine learning algorithms.

## Table of Contents

- [Project Overview](#project-overview)
- [Models Used](#models-used)
- [Performance Comparison](#performance-comparison)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Credit card fraud is a significant problem in the financial industry. The goal of this project is to create a reliable and accurate model to classify transactions as fraudulent or legitimate. The models are trained on historical transaction data and evaluated based on various performance metrics.

## Models Used

The following machine learning models were used and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
- Naive Bayes
- Support Vector Machine (SVM) (Practically Infeasible To synthesis for such a large dataset)
- LightGBM (Light Gradient Boosting Machine)

## Performance Comparison

The models were compared based on accuracy, mean absolute error, confusion matrix, and classification report. The Random Forest model was selected as the best-performing model for this project.

### Performance Metrics

| Model              | Accuracy | Mean Absolute Error | Precision | Recall | F1-Score |
|--------------------|----------|---------------------|-----------|--------|----------|
| Logistic Regression| 0.9955   | 0.0094              | 1.00      | 0.00   | 0.50     |
| Decision Tree      | 0.9980   | 0.0020              | 1.00      | 0.79   | 0.88     |
| Random Forest      | 0.9989   | 0.0023              | 1.00      | 0.77   | 0.92     |
| KNN                | 0.9972   | 0.0043              | 1.00      | 0.49   | 0.79     |
| Naive Bayes        | 0.9922   | 0.0096              | 0.99      | 0.47   | 0.66     |
| LightGBM           | 0.9984   | 0.0024              | 1.00      | 0.74   | 0.89     |

Based on the above, Random Forest Model is used for prediction.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/agneepradeep/Afame-Technologies.git
   cd credit-card-fraud-detection
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

## Licence
This project is licensed under the MIT License. See the [LICENSE file](LICENSE.md) for details.
