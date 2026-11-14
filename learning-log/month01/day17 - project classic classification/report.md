# Classical Classification Experiment

## 1. Objective
Compare Logistic Regression and Decision Tree classifiers on the Breast Cancer Wisconsin Diagnostic Dataset.

## 2. Dataset
- Number of samples: 569
- Number of features: 30
- Classification type: Binary
- Target classes: Malignant and Benign

## 3. Experimental Setup
- Training/testing split: 80/20
- Random state: 42
- Stratified splitting: Yes
- Evaluation: Accuracy, Precision, Recall, F1-score

## 4. Models
### Logistic Regression

Logistic Regression is a supervised classification algorithm that predicts the probability of a sample belonging to a class using the sigmoid function. A threshold of 0.5 is used to assign the predicted class.

**Preprocessing:** The dataset was split into training and testing sets using stratified sampling. `StandardScaler` was applied to standardize features, ensuring they have a similar scale. Both steps were included in a Scikit-learn pipeline to prevent data leakage.

**Configuration:** The model used `LogisticRegression(max_iter=5000)` to allow sufficient iterations for convergence. The model was trained on the training data and evaluated on the test data.

### Decision Tree

A Decision Tree is a supervised classification algorithm that makes predictions by splitting data into smaller groups based on feature values. Each internal node represents a decision, each branch represents an outcome, and each leaf represents a predicted class.

**Configuration:** The model used `DecisionTreeClassifier(max_depth=4, random_state=42)`. The maximum depth was limited to 4 to reduce model complexity and help prevent overfitting.

## 5. Results
### 1. Logistic Regression

**Evaluation Metrics:**

| Metric | Score |
|---|---:|
| Accuracy | 0.9825 (98.25%) |
| Precision | 0.9861 (98.61%) |
| Recall | 0.9861 (98.61%) |
| F1-score | 0.9861 (98.61%) |

**Confusion Matrix:**

```text
[[41  1]
 [ 1 71]]
```

**Classification Report:**

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Malignant (Yes) | 0.98 | 0.98 | 0.98 | 42 |
| Benign (No) | 0.99 | 0.99 | 0.99 | 72 |
| **Accuracy** | | | **0.98** | **114** |
| Macro Avg | 0.98 | 0.98 | 0.98 | 114 |
| Weighted Avg | 0.98 | 0.98 | 0.98 | 114 |

### 2. Decision Tree

**Evaluation Metrics:**

| Metric | Score |
|---|---:|
| Accuracy | 0.9386 (93.86%) |
| Precision | 0.9577 (95.77%) |
| Recall | 0.9444 (94.44%) |
| F1-score | 0.9510 (95.10%) |

**Confusion Matrix:**

```text
[[39  3]
 [ 4 68]]
```

**Classification Report:**

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Malignant (Yes) | 0.91 | 0.93 | 0.92 | 42 |
| Benign (No) | 0.96 | 0.94 | 0.95 | 72 |
| **Accuracy** | | | **0.94** | **114** |
| Macro Avg | 0.93 | 0.94 | 0.93 | 114 |
| Weighted Avg | 0.94 | 0.94 | 0.94 | 114 |

### 3. Model Comparison

| Metric | Logistic Regression | Decision Tree |
|---|---:|---:|
| Accuracy | 98.25% | 93.86% |
| Precision | 98.61% | 95.77% |
| Recall | 98.61% | 94.44% |
| F1-score | 98.61% | 95.10% |


### 6. Analysis and Observations

**1. Which model had higher malignant-class recall?**

Logistic Regression had higher malignant-class recall at **0.98 (98%)**, compared to **0.93 (93%)** for the Decision Tree. Therefore, Logistic Regression identified more malignant cases correctly in this test set.

**2. What were the main differences?**

Logistic Regression performed better across all evaluation metrics, achieving 98.25% accuracy and a 98.61% F1-score. The Decision Tree achieved 93.86% accuracy and a 95.10% F1-score. Logistic Regression also produced fewer misclassifications, with 2 errors compared to 7 for the Decision Tree.

## 7. Conclusion

Logistic Regression outperformed the Decision Tree in this experiment, achieving higher accuracy, precision, recall, and F1-score. It also detected more malignant cases correctly. Based on this test set, Logistic Regression was the better-performing model. However, further evaluation using cross-validation and hyperparameter tuning is needed to confirm its performance.

## 8. Limitations
- The evaluation used only one train-test split, so results may vary with different splits.
- The dataset was relatively small, containing 569 samples.
- The Decision Tree was limited to a maximum depth of 4, which may have restricted its ability to learn complex patterns.
- High test accuracy does not guarantee good performance on unseen real-world data.
- The experiment did not include cross-validation or hyperparameter tuning.
