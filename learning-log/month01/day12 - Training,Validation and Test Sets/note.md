1. Why do we divide datasets? <br>
+ so that data for training, validating, and testing will be different. <br>
+ to know how does our model will work in unseen data<br> <br>

2. What is the difference between training and validation? <br>
+ training means  observing pattern and doing calculation, to learn the model parameter like weight and biasness  <br>
+ validation means doing hyperparameter tuning for better prediction. <br> <br>

3. Why should the test set be used only for final evaluation? <br>
+ to prevent the overfitting and data leakage. <br> <br>

4. What is overfitting? <br>
+ The condition in which the model memorized the whole pattern of the data with its noise. <br>
+ zero or less error in training data, but high error in testing data
<br>
<br>
5.What is underfitting? <br>
+ The condition in which model cannot learn the pattern of the data. <br>
+ high error in both training and test data. <br> <br>

6.What is data leakage? <br>
+ When the important and legimited information leaked pior to the model which can mislead the testing, then it is data leakage.<br> <br>

7. Why is random_state useful? <br>
+ It helps to prevent the randomness of data each time. <br> <br>

8. What happens when a decision tree becomes too complex?<br>
+  Overfitting
