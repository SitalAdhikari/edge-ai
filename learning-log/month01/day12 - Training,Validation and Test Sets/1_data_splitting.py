import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression

#make a sample regression dataset:
X,y = make_regression(
	n_samples=100,
	n_features=3,
	noise=20,
	random_state=42
)
print(X.shape)
print(y.shape)

print("Firt split: separate test data")
X_temp,X_test,y_temp,y_test= train_test_split(X,y,test_size=0.15, random_state=42)
print("Second split: separate validation data")
X_train,X_val,y_train,y_val = train_test_split(X_temp,y_temp,test_size=0.1765, random_state=42)

print("\n Dataset Division:")
print("Training:",X_train.shape)
print("Testing:",X_test.shape)
print("Validation:",X_val.shape)

# 15% -validation set
# 15% - testing set
#70% - training set
