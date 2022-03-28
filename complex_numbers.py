from __future__ import annotations


class ComplexNumber:
    def __init__(self, real: int, imaginary: int):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other: ComplexNumber):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other: ComplexNumber):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other: ComplexNumber):
        return ComplexNumber(self.real + ((self.imaginary * other.imaginary) * -1), self.imaginary+(self.real *
                                                                                                    other.real))

    def __sub__(self, other: ComplexNumber):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other: ComplexNumber):
        pass

    def __abs__(self):
        pass

    def conjugate(self):
        self.imaginary *= (-1)
        return self

    def exp(self):
        pass


c = ComplexNumber(1, -3)
x = ComplexNumber(2, 5)

print(c.__mul__(x).real)
print(c.__mul__(x).imaginary)
