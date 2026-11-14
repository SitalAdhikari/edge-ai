from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
	accuracy_score,
	classification_report,
	confusion_matrix,
)

dataset = load_breast_cancer()

X= dataset.data
y=dataset.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42, stratify=y)

model = Pipeline([
	("scaler", StandardScaler()),
	("classifier", LogisticRegression())
	
])

model.fit(X_train,y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_pred,y_test)

print("Accuracy:",accuracy)
print("\n Classification Report:")
print(
	classification_report(
		y_test,
		y_pred,
		target_names = dataset.target_names
	)
)

print("Confusion Matrix: ")
print(confusion_matrix(y_pred,y_test))

# probability of either [0  and  1] 
probabilities = model.predict_proba(X_test[:5])
print("Predicted probabilities:")
print(probabilities)


# each feature has different mean and st.deviation , so mulitple values of mean and st.dev
scaler = model.named_steps['scaler']
print("Mean:", scaler.mean_)
print("St. deviaton: ", scaler.scale_)
