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

## Results Summary

| Metric | Logistic Regression | Decision Tree |
|---|---:|---:|
| Accuracy | 98.25% | 93.86% |
| Precision | 98.61% | 95.77% |
| Recall | 98.61% | 94.44% |
| F1-score | 98.61% | 95.10% |

Logistic Regression performed better across all four evaluation metrics on the test set.

## Project Structure

```text
classification-project/
├── results/
│   └── result.md
├── src/
│   └── train.py
├── report.md
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

## Detailed Report

See [report.md](report.md) for the methodology, evaluation results, model comparison, limitations, and conclusion.

## Learning Outcomes

- Understood the fundamentals of classification.
- Implemented Logistic Regression and Decision Tree models.
- Learned feature scaling and Scikit-learn pipelines.
- Evaluated models using classification metrics and confusion matrices.
- Compared model performance and identified limitations.
