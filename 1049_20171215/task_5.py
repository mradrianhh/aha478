class Polynom:
    _polynom = {}

    def __init__(self, polynom):
        self._polynom = polynom

    def get_polynom(self):
        return self._polynom

    def __str__(self):
        result = ""
        polynom = self.get_polynom()
        for key in polynom:
            if key == 0:
                result += f"{polynom[key]} + "
            else:
                result += f"{polynom[key]}x^{key} + "
        return result[:len(result)-2]

    def __call__(self,x):
        total = 0
        polynom = self.get_polynom()
        for key in polynom:
            total += polynom[key]*x**key
        return total

    def __add__(self, p):
        result = self.get_polynom()
        polynom = p.get_polynom()
        for key in polynom:
            if key in result:
                result[key] += polynom[key]
            else:
                result[key] = polynom[key]

        return Polynom(result)


if __name__ == "__main__":
    p = Polynom({0: 3, 3: 2, 7: -4})
    print(p)
    print(p(3))

    p1 = Polynom({1: 3, 3: -2})
    p2 = Polynom({2: 2, 3: 3, 5: -2})
    p3 = p1 + p2
    print(str(p3))
    print(p3(1))