from math import pi

#a)
def ellipsePerimeter(r1, r2):
    return 2*pi*((r1**2 + r2**2)/2)**0.5

print(ellipsePerimeter(10,10))

#b) og c)
def xq(a, b, c):
    if a == 0:
       raise ValueError("Can't divide by 0.")
    
    x1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
    x2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
    return (x1, x2)

print(xq(0, 2, 1))