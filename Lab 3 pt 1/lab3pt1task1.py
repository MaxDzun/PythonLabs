# Task 1. Modify the class Rational of Lab No1 to perform the following tasks:
# - adding two Rational numbers. The result should be stored in reduced form;
# - subtracting two Rational numbers. The result should be stored in reduced form;
# - multiplying two Rational numbers. The result should be stored in reduced form;
# - dividing two Rational numbers. The result should be stored in reduced form;
# - comparison two Rational numbers.
from math import gcd

class Rational:

    def __init__(self, numerator=1, denominator=4):
        if denominator == 0:
            raise ZeroDivisionError("Division by zero")
        if not isinstance(numerator, int):
            raise TypeError("Invalid numerator")
        else:
            self.__numerator = numerator
        if not isinstance(denominator, int):
            raise TypeError("Invalid denominator")
        else:
            self.__denominator = denominator

# previous (from lab 1) functions:
    def fraction(self):
        self.__gcd = gcd(self.__numerator, self.__denominator)
        self.__reduced_numerator = self.__numerator // self.__gcd
        self.__reduced_denominator = self.__denominator // self.__gcd
        return f"{self.__reduced_numerator}/{self.__reduced_denominator}"

    def floating_fraction(self):
        float_fraction = self.__reduced_numerator / self.__reduced_denominator
        return f"{float_fraction:.{3}f}"

# new functions:
    def __mul__(self, other):
        numerator = self.__numerator * other.__numerator
        denominator = self.__denominator * other.__denominator
        return "Multiply result", Rational(numerator, denominator).fraction()

    def __truediv__(self, other):
        numerator = self.__numerator * other.__denominator
        denominator = self.__denominator * other.__numerator
        return "Divide result", Rational(numerator, denominator).fraction()

    def __add__(self, other):
        numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        denominator = self.__denominator * other.__denominator
        return "Add result", Rational(numerator, denominator).fraction()

    def __sub__(self, other):
        numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        denominator = self.__denominator * other.__denominator
        return "Substract result", Rational(numerator, denominator).fraction()

    def __lt__(self, other):
        return self.floating_fraction() < other.floating_fraction()

    def __le__(self, other):
        return self.floating_fraction() <= other.floating_fraction()

    def __gt__(self, other):
        return self.floating_fraction() > other.floating_fraction()

    def __ge__(self, other):
        return self.floating_fraction() >= other.floating_fraction()

fr1 = Rational(15,63)
fr2 = Rational(1,12)
fr3 = Rational(7,23)
fr4 = Rational(4,9)

print("fraction 1: ",fr1.fraction()," or ",fr1.floating_fraction())
print("fraction 2: ",fr2.fraction()," or ",fr2.floating_fraction())
print("fraction 3: ",fr3.fraction()," or ",fr3.floating_fraction())
print("fraction 4: ",fr4.fraction()," or ",fr4.floating_fraction())

print(fr1 * fr3)
print(fr4 / fr1)
print(fr2 + fr3)
print(fr3 - fr4)
print(fr3 > fr4)
print(fr2 >= fr4)
print(fr1 < fr4)
print(fr2 <= fr4)


