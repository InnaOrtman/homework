# Task 3
# Fraction
# Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *)
# with appropriate checking and error handling

# class Fraction:
# pass

# x = Fraction(1/2)
#
# y = Fraction(1/4)
#
# x + y == Fraction(3/4)

class Fraction:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('wrong value')
        return Fraction(self.value + other.value)

    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('wrong value')
        return Fraction(self.value - other.value)

    def __mul__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('wrong value')
        return Fraction(self.value * other.value)

    def __div__(self, other) -> object:
        if not isinstance(other, type(self)):
            raise ValueError('wrong value')
        if self.value != 0:
            self.value = self.value
        else:
            raise ZeroDivisionError
        return Fraction(self.value / other.value)

    def __str__(self):
        return f'<Fraction: {self.value}>'

    def __repr__(self):
        return self.__str__()


x = Fraction(1 / 2)
y = Fraction(1 / 4)

print(x + y)

