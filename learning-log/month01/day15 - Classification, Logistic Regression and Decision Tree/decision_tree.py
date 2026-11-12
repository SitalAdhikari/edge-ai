from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

data = load_breast_cancer()
X= data.data
y= data.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=42,stratify=y)
# stratify = y:: Both datasets(train and test) maintain the original  ratio of classes

depths= [1,2,3,5,10,None]

for depth in depths:
	model = DecisionTreeClassifier(criterion='entropy',max_depth=depth,random_state=42)
	model.fit(X_train,y_train)
	y_pred_train = model.predict(X_train)
	y_pred_test = model.predict(X_test)
	accuracy_train = accuracy_score(y_pred_train,y_train)
	accuracy_test = accuracy_score(y_pred_test,y_test)
	print(f"Depth:{depth} | Accuracy_Train:{accuracy_train} | Accuracy_Test: {accuracy_test}")


"""plot_tree(
	model,
	feature_names = data.feature_names,
	class_names= data.target_names,
	filled=True,
	rounded=True,
	fontsize=8
)

plt.title("Decision Tree Classifier")
plt.show() """



"""Output:
Depth:1 | Accuracy_Train:0.9230769230769231 | Accuracy_Test: 0.9210526315789473
Depth:2 | Accuracy_Train:0.9582417582417583 | Accuracy_Test: 0.8947368421052632
Depth:3 | Accuracy_Train:0.967032967032967 | Accuracy_Test: 0.9473684210526315
Depth:5 | Accuracy_Train:0.9912087912087912 | Accuracy_Test: 0.9298245614035088
Depth:10 | Accuracy_Train:1.0 | Accuracy_Test: 0.9122807017543859
Depth:None | Accuracy_Train:1.0 | Accuracy_Test: 0.9122807017543859 """

# Depth:3 gave better answer without over and underfitting.
