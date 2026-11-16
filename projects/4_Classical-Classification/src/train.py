import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_validate, GridSearchCV
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

tree_model = Pipeline([
	("classifier", DecisionTreeClassifier(random_state=42))
])

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scoring = ['accuracy','f1_macro','recall_macro','precision_macro']

logistic_score = cross_validate(logistic_model,X_train,y_train,cv=cv,scoring=scoring)
tree_score = cross_validate(tree_model,X_train,y_train,cv=cv,scoring=scoring)

def display_cv_results(name,scores):
	print(name)
	for metric in scoring:
		values = scores[f"test_{metric}"]
		print(f"{metric} :{np.mean(values): .4f} +/-{np.std(values): .4f} ")
display_cv_results("Logistic Regression:", logistic_score)
display_cv_results("Decision Tree: ", tree_score)

#hyperparameter tuning:
param_grid = {
	"classifier__C": [ 0.01,0.1,0.9,1,1.1,10],
	"classifier__l1_ratio":[0,1],
	"classifier__solver":["liblinear"]
}
grid_search = GridSearchCV(
	estimator = logistic_model,
	param_grid=param_grid,
	cv=cv,
	scoring='f1_macro',
	n_jobs=-1,
	
)
grid_search.fit(X_train,y_train)
print("Best parameters:", grid_search.best_params_)
print("Best CV F1 macro:", grid_search.best_score_)

#evaluation
best_logistic = grid_search.best_estimator_
tree_model.fit(X_train,y_train)

logistic_prediction = best_logistic.predict(X_test)
tree_prediction = tree_model.predict(X_test)

def evaluate_model(name,y_true,y_pred):
	print("\n", {name})
	print("Accuracy:",accuracy_score(y_true,y_pred))
	print("Precision (macro):", precision_score(y_true,y_pred,average='macro'))
	print("F1 (macro):", f1_score(y_true,y_pred,average='macro'))
	print("Recall (macro):", recall_score(y_true,y_pred,average='macro'))
	print("Confusion matrix:", confusion_matrix(y_true,y_pred))

evaluate_model("logistic regression tuned",y_test, logistic_prediction)
evaluate_model("Decision Tree", y_test,tree_prediction)


models = {
	"Logistic Regression": logistic_prediction,
	"Decision Tree": tree_prediction
}
rows=[]
for name,predictions in models.items():
	rows.append({
		"model": name,
		"Accuracy": accuracy_score(y_test,predictions),
		"Precision (macro)": precision_score(y_test,predictions,average='macro'),
		"F1 (macro)": f1_score(y_test,predictions,average='macro'),
		"Recall (macro)": recall_score(y_test,predictions,average='macro')
	})
results = pd.DataFrame(rows)

results_dir = Path("results")
results_dir.mkdir(parents=True,exist_ok=True)
results.to_csv(results_dir/"metrics.csv",index=False)
