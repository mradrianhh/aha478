def integrate(f, a, b, n=100):
    total = 0
    for k in range(1, n):
        total += f(a+k(b-a)/n)

    return ((b-a)/n) * ( f(a)/2 + total + f(b)/2 )

result = integrate(lambda x: 2*x, 0, 5)
print(result)