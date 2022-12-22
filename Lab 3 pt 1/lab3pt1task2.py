# Task 2.
# TВ-11
# Create a class CALENDAR. Define methods for creating and working with a CALENDAR instances and overload operations^
# "+=, -=" - for adding and subtracting days, months, years to a given date
# "==, ! =, >, >=, <, <=" - for comparing dates.
import datetime

class Calendar:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not isinstance(day, int) and day >= 1:
            raise TypeError("Invalid day")
        self.__day = day

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if not isinstance(month, int) and month >= 1:
            raise TypeError("Invalid month")
        self.__month = month

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if not isinstance(year, int) and year >= 1:
            raise TypeError("Invalid year")
        self.__year = year

    def date(self):
        return datetime.datetime(self.__year, self.__month, self.__day)

    def __gt__(self, other):
        return self.date() > other.date()

    def __ge__(self, other):
        return self.date() >= other.date()

    def __lt__(self, other):
        return self.date() < other.date()

    def __le__(self, other):
        return self.date() <= other.date()

    def __ne__(self, other):
        return self.date() != other.date()

    def __eq__(self, other):
        return self.date() == other.date()

    def __isub__(self, other):
        [d, m, y] = other
        if not isinstance(d, int):
            raise TypeError("Invalid day")
        if not isinstance(m, int):
            raise TypeError("Invalid month")
        if not isinstance(y, int):
            raise TypeError("Invalid year")
        if d > self.__day:
            self.__day = 30 - (self.__day - d)
            self.__month -= 1
        if m > self.__month:
            self.__month = 12 - (self.__month - m)
            self.__month -= 1
        if y > self.__year:
            raise ValueError("Invalid year")

        self.__month -= m
        self.__year -= y
        self.__day -= d
        return self

    def __iadd__(self, other):
        [d, m, y] = other
        if not isinstance(d, int):
            raise TypeError("Invalid day")
        if not isinstance(m, int):
            raise TypeError("Invalid month")
        if not isinstance(y, int):
            raise TypeError("Wrong value of year")

        if d + self.__day > 30:
            self.__day = (self.__day + d) - 30
            self.__month += 1
        else:
            self.__day += d
        if m + self.__month > 12:
            self.__month = (self.__month + d) - 12
            self.__year += 1
        else:
            self.__month += m

        self.__year += y
        return self

    def __str__(self):
        return f'{self.__day}.{self.__month}.{self.__year}'


d1 = Calendar(14, 9, 1814)
d2 = Calendar(21, 12, 2022)
d3 = Calendar(1, 1, 1001)

print("first date", d1)
print("second date", d2)
print("third date", d3)

d1 += [16, 0, 16]
print(d1)
d2 -= [9, 2, 20]
print(d2)
# d3 -= [-2, 0, 0]
d3 = d3.date()
print(d3)

print(d2 != d1)
print(d2 >= d1)
print(d3 == d2)

