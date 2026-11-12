from sklearn.metrics import (
	confusion_matrix,
	accuracy_score,
	f1_score,
	recall_score,
	precision_score,
	classification_report
)

y_true = ( [1]* 45 + [0]*55)
y_pred = ([1]*40+[0]*5+[1]*10 + [0]*45)
# y_pred = TP + FP +FN +TN

cm = confusion_matrix(y_true,y_pred)
print("Confusion matrix:", cm)
accuracy = accuracy_score(y_pred,y_true)
precision = precision_score(y_true,y_pred)
recall=recall_score(y_true,y_pred)
f1= f1_score(y_true,y_pred)

print(f"Accuracy:{accuracy}")
print(f"Precision:{precision}")
print(f"Recall:{recall}")
print(f"f1:{f1}")

print(classification_report(
	y_true,y_pred,target_names=['Non Defective', 'Defective'], zero_division=0
))
