import numpy as np
from math import pi as PI
import matplotlib.pyplot as plt

x_vals = np.linspace(-10*PI, 10*PI, 200) # create 200 evenly spaced values from -10PI to 10PI.
f_vals = np.sin(x_vals)*np.sqrt(np.abs(x_vals))/(x_vals**2 + 1) # using numpy-functions that manipulate the entire array to calculate f_vals.
plt.plot(x_vals, f_vals) # plot x_vals against f_vals and show the plot.
plt.show()