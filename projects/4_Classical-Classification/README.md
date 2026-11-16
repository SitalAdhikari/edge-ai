# Classical Classification Experiment

## Overview
This project compares two classical machine learning classification algorithms using the Breast Cancer Wisconsin Diagnostic dataset from Scikit-learn.

The objective is to train and evaluate Logistic Regression and Decision Tree models and compare their classification performance.

## Dataset
- **Source:** Scikit-learn Breast Cancer Wisconsin Diagnostic dataset
- **Samples:** 569
- **Features:** 30 numerical features
- **Classes:** Malignant and Benign

## Models Used

### 1. Logistic Regression
- Used `StandardScaler` for feature scaling.
- Implemented using a Scikit-learn preprocessing pipeline.
- Maximum iterations: 5000.
- Hyperparameter tuned

### 2. Decision Tree
- Implemented using `DecisionTreeClassifier`.
- Maximum tree depth: 4.
- Random state: 42.

## Evaluation Metrics
Both models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix


## Project Structure

```text
classification-project/
├── results/
│   └── result.md
├── src/
│   └── train.py
├── requirements.txt
└── README.md
```

## How to Run

1. Install the required libraries:

```bash
pip install numpy pandas matplotlib scikit-learn
```

2. Run the project:

```bash
python src/train.py
```

3. View the generated confusion matrices in the `results/` directory.


## Learning Outcomes

- Understood the fundamentals of classification.
- Implemented Logistic Regression and Decision Tree models.
- Learned feature scaling, Scikit-learn pipelines, cross validation and hyperparameter tuned.
- Evaluated models using classification metrics and confusion matrices.
- Compared model performance and identified limitations.
