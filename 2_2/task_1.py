import numpy as np

# Creates a ndarray of shape (100, ) with np.arange, then reshapes it into a ndarray of shape (10, 10).
x = np.arange(-49, 51).reshape((10, 10))
print(x<0)

print("\n")

y = (x**2 - 500) > 0
print(y)

x[y] = 0
print(x)

a = np.where(True,y,x)
a[True] = np.nan
a[False] = x**2 - 0.2
print(a)