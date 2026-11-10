# Day12 - Training, Validation, and Test Sets

-Why datasets are divided. <br>
- Training vs Testing <br>
- Validationdata and model selection <br>
- Overfitting and underfitting: causes and solution : bias and variance <br>

- Data leakage <br>
```
	Prevent the data leakage:
	- Split before fitting preprocessing transformations.
	- Never fit a model on test data.
	- Never use test results to repeatedly tune the model.
	- Use pipelines to keep preprocessing and model training correctly separated.

```
