import math
from scipy.misc import derivative

class ThirdDerivative():

    function = None

    def __init__(self, function):
        self.function = function

    def calculate(self, x, h=0.0001):
        return (-0.5*self.function(x-2*h) + self.function(x-h) - self.function(x+h) + 0.5*(self.function(x+2*h))) / h**3

if __name__ == "__main__":
    print(ThirdDerivative(lambda x: math.cos(x)).calculate(0))
    print(derivative(lambda x: math.cos(x), 0))
    