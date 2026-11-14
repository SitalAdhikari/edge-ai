import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
	accuracy_score, f1_score, recall_score, precision_score, classification_report, confusion_matrix
)

data = load_breast_cancer()
X= data.data
y=data.target

#dataframe
df = pd.DataFrame(X, columns = data.feature_names)
df['target'] = y
print("Dataset Shape:",df.shape)
print("Feature names:", data.feature_names)
print("Target Distribution:", df['target'].value_counts())

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=42, stratify=y)

logistic_model = Pipeline([
	("scaler",StandardScaler()),
	("classifier", LogisticRegression(max_iter=5000))
])

logistic_model.fit(X_train,y_train)
logistic_pred = logistic_model.predict(X_test)

tree_model = DecisionTreeClassifier( max_depth =4, random_state=42)
tree_model.fit(X_train,y_train)
tree_pred= tree_model.predict(X_test)

# evaluation:

	
	
def evaluate_model(name,y_test,y_pred):
	
	result = {
		"Model Name": name,
		"Accuracy Score": accuracy_score(y_test,y_pred),
		"F1 score": f1_score(y_test,y_pred),
		"Recall score": recall_score(y_test,y_pred),
		"Precision":precision_score(y_test,y_pred),
	}
	with open("results/metrics.md","a") as file:
		writer=csv.writer(file)
		for metric,value in result.items():
			writer.writerow([metric,value])
	
	for metric, value in result.items():
		print(metric ,":",value)
	print("Confusion Matrix:", confusion_matrix(y_test,y_pred))
	print(
		classification_report(
			y_test,y_pred,target_names=['Malignant(Yes)','Benign (No)']
		)
	)

evaluate_model("LogisticRegression",y_test,logistic_pred)
evaluate_model("DecisionTree",y_test,tree_pred)

	




# plot the confusion matrix in the heatmap::
from sklearn.metrics import ConfusionMatrixDisplay

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

ConfusionMatrixDisplay.from_predictions(
    y_test,
    logistic_pred,
    display_labels=["Malignant", "Benign"],
    ax=axes[0],
    cmap="Blues"
)

axes[0].set_title("Logistic Regression")

ConfusionMatrixDisplay.from_predictions(
    y_test,
    tree_pred,
    display_labels=["Malignant", "Benign"],
    ax=axes[1],
    cmap="Greens"
)

axes[1].set_title("Decision Tree")

plt.tight_layout()
plt.savefig(
    "results/confusion_matrices.png",
    dpi=300
)

plt.show()
