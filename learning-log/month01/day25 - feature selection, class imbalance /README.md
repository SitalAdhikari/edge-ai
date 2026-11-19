# day25 

- Feature Engineering: creating or combining existing information to produce more useful features.
```
	height, weight , ::: then we can introducte: bmi : where bmi = weight / square(height)
	
```
- Feature extraction: transforming existing data into a new representation that captures useful information. <br>
- Feature Transfomation: it changes how esiting features are represented: 
```
	For eg: Standarization, Normalization, Log transfomation
```
- Feature Selection: select the certain imp features
```
	-filter method: correlation, chi-square test, anova f-test, mutual information
	- wrapper methods - train and evaluate a model and decide : computationally expensive
	- embedded methods - as a process of model training: l1 regularization, decision tree feature imp, random forest feature importance
```
- Resampling Technique:
```
	1. Random Oversampling: duplicates radnoly selected minority class samples:  overfitting increases
	2. Random Undersampling: removes randomly selected majority class samples: can discard useful information.
	3. SMOTE : generates synthetic minority samples using interpolation between neighboring minority class samples:
	4. Class Weights: assigns greater importance to minority calss errors during model training,
```

