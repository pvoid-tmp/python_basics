# Lesson 8 task 7

class MyComplex:

    def __init__(self, real=0.0, imaginary=0.0):
        self.real = float(real)
        self.imaginary = float(imaginary)

    def __str__(self):
        if self.imaginary == 0.0:
            return f"{self.real:.2f}"
        if self.real == 0.0:
            return f"({self.imaginary:.2f}i)"
        i_sign = '-' if self.imaginary < 0.0 else '+'
        return f"({self.real:.2f}{i_sign}{abs(self.imaginary):.2f}i)"

    def __add__(self, other):
        return MyComplex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return MyComplex(self.real * other.real - self.imaginary * other.imaginary,
                         self.imaginary * other.real + self.real * other.imaginary)


# main
n0 = MyComplex()
n1 = MyComplex(1.111, 2.222)
n2 = MyComplex(-3.333, 4.444)
n3 = MyComplex(5.555, -6.666)
n4 = MyComplex(7.777, -8.888)
n5 = MyComplex(-7.777, 8.888)
n6 = MyComplex(0.0, 9.999)
n7 = MyComplex(-100.0)
print(n0, n1, n2, n3, n4, n5, n6, sep="; ")
print(f"{n0} + {n0} = {n0 + n0}")
print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n4} + {n5} = {n4 + n5}")
print(f"{n1} + {n2} + {n3} + {n4} = {n1 + n2 + n3 + n4}")
print(f"{n1} * {n2} = {n1 * n2}")
print(f"{n1} * {n2} * {n3} = {n1 * n2 * n3}")
print(f"{n4} * {n0} = {n4 * n0}")
print(f"{n6} * {n7} = {n6 * n7}")
print(f"{n1} * {n2} + {n3} * {n4} = {n1 * n2 + n3 * n4}")
