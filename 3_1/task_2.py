class Vector3D():
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Cube():
    
    _dimension = Vector3D(0,0,0)
    density = 0

    def __init__(self, x, y, z, d=997):
        self.set_dimension(Vector3D(x, y, z))
        self.density = d

    def set_dimension(self, dimension):
        self.dimension = dimension

    def get_dimension(self):
        return self.dimension

    def volume(self):
        dimension = self.get_dimension()
        return dimension.x * dimension.y * dimension.z

    def area(self):
        dimension = self.get_dimension()
        return 2*(dimension.x*dimension.y + dimension.x*dimension.z + dimension.y*dimension.z)

    def mass(self):
        return self.volume() * self.density

if __name__ == "__main__":
    silica_aerogel = Cube(2, 0.5, 0.5, 1.9)
    print(f"Volume: {silica_aerogel.volume()}, Area: {silica_aerogel.area()}, Mass: {silica_aerogel.mass()}")

    water = Cube(2, 0.5, 0.5)
    print(f"Volume: {water.volume()}, Area: {water.area()}, Mass: {water.mass()}")

    print("Is the water cube heavier then the silica-areogel cube?")
    if water.mass() > silica_aerogel.mass():
        print("Well, yes, indeed it is!")
    else:
        print("No, it is not...*sadface*")

