import numpy as np

# Creates a ndarray of shape (100, ) with np.arange, then reshapes it into a ndarray of shape (10, 10).
x = np.arange(-49, 51).reshape((10, 10))
print(x<0)

# Creates a new array of boolean values determined by the evaluation the boolean expression.
y = (x**2 - 500) > 0

# Sets every value in x that satifies the boolean expression given by y to 0.
x[y] = 0

# Loops through y and checks if its True, if it is, set the value to np.nan, else, x^2-0.2.
z = np.where(y, np.nan, x**2-0.2)