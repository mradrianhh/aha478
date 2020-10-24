import math
from scipy.misc import derivative
import numpy as np
from matplotlib import pyplot as plt

class ThirdDerivative():

    function = None

    def __init__(self, function):
        self.function = function

    def calculate(self, x, h=0.0001):
        return (-0.5*self.function(x-2*h) + self.function(x-h) - self.function(x+h) + 0.5*(self.function(x+2*h))) / h**3

if __name__ == "__main__":

    x = np.linspace(0, 10)

    plt.plot(x, ThirdDerivative(lambda x: np.cos(x)).calculate(x), label="Appromixation")
    plt.plot(x, derivative(lambda x: np.cos(x), x, n=3, order=5), label="Exact")
    plt.legend()
    plt.show()
    