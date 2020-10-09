import math

#a)
def func1(x, y):
    return math.sin(x)*math.cos(y)

print(func1(math.pi/2, 0))

#b) og c)
def func2(x):
    if math.fabs(x) == 2:
        raise ValueError("Can't divide by zero.")
    else:
        return (x**2-1)**0.5/(4-x**2)

print(func2(2))