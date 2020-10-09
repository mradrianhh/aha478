def derivative(f, x, h=1E-5):
    return (f(x+h) - f(x))/h

print(derivative(lambda x: x**2, 2))