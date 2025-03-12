'''
# Why ML Problems are a statistical Inference Problem ?
Question Understanding: With the help of sample, we try to find the estimate value for the value <-- this is called statistical inference problem.
Ans:- lpa = f`(cgpa, iq) + reducible_error + irreducible_error
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
print(y_pred)

# Plot the scatter plot and regresssion lines. 
plt.scatter(x, y, label="Data Points")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Scatter plot with increased variability and regression lines")

# Plot the scatter plot and regression lines. 
x_line = np.linspace(0, 10, 100)
y_actual = 2 * x_line - 5
plt.plot(x_line, y_actual, 'r', label="Population line (m=3, b=-8)")

# Plot the estimated regression line. 
y_estimated = model.coef_[0] * x_line + model.intercept_
plt.plot(x_line, y_estimated, 'g', label=f"Estimated line (m={model.coef_[0]:.2f}, b={model.intercept_:.2f})")

# Add legend and show the plot
plt.legend()
plt.show()
