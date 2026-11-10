import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# generating data with random relationship
rng = np.random.default_rng(42)

X = np.linspace(0,10,100).reshape(-1,1)
# -1: automatically calculate the size of this dimension based on the total number of elements and the other dimensions
# 1: The resulting shape changes from (100,) (1D) to (100, 1) (2D: 100 rows and 1 column).
# (100,) is a list, and (100,1) is a column vector
y = np.sin(X).ravel() + rng.normal(0,0.1,size=100)
#Computes sin(X) (the true underlying function), flattens it to 1-D, and adds Gaussian noise (mean 0, std 0.1) to simulate real-world measurement error.

# above why we have done complex instead of make_regression coz to make  cury pattern instead of st.line
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

for depth in [1,3,None]:
	model = DecisionTreeRegressor(max_depth=depth,random_state=42)
	model.fit(X_train,y_train)
	
	train_predicitons = model.predict(X_train)
	test_predictions= model.predict(X_test)
	
	train_error = mean_squared_error(y_train,train_predicitons)
	test_error = mean_squared_error(y_test,test_predictions)
	
	print("\n Tree depth:", depth)
	print("Training MSE:",train_error)
	print("Testing MSE:",test_error)
	
	
# Tree depth: 1 #underfitting -> high error on both
# Training MSE: 0.31596797141315014
# Testing MSE: 0.47843040275676474

# Tree depth: 3 # best -> low error in both
# Training MSE: 0.0530247862107467
# Testing MSE: 0.05552378475991091

# Tree depth: None # overfitting -> trainingerror drop to zero
# Training MSE: 0.0 
# Testing MSE: 0.014842966045272663


