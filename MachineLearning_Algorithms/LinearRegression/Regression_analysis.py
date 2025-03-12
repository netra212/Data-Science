'''
# Why ML Problems are a statistical Inference Problem ?
Question Understanding: With the help of sample, we try to find the estimate value for the value <-- this is called statistical inference problem.
Ans:- 
lpa = f`(cgpa, iq) + reducible_error + irreducible_error
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generating the data. 
x = 10 * np.random.rand(50)
y = 3 * x - 8 + np.random.randn(50) * 4 # y = 2x - 8 + some_randomness.

# Fit a linear regression model.
x = x.reshape(-1, 1)
model = LinearRegression()
mode.fit(x, y)

# Calculate the predicted values. 
y_pred = model.predict(x)

# Plot the scatter plot and regresssion lines. 





