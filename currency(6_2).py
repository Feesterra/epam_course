#!/usr/bin/env python3.6

from abc import ABCMeta


class Currency(metaclass=ABCMeta):
    """Abstract class for currencies."""

    symbol = None
    value = 0

    def __init__(self, money):
        """Class constructor.

        :param money: actual amount of money.
        :type money: int or float
        """

        self.money = money

    def __repr__(self):
        """Defines printing.

        :returns: string s"""

        s = '{0} {1}'.format(self.money, self.symbol)
        return s

    def __eq__(self, other):
        """Redefines operator ==."""

        return self.money == other.money

    def __le__(self, other):
        """Redefines operator <=."""

        return self.money <= other.money

    def __ge__(self, other):
        """Redefines operator >=."""

        return self.money >= other.money

    def __lt__(self, other):
        """Redefines operator <."""

        return self.money < other.money

    def __gt__(self, other):
        """Redefines operator >."""

        return self.money > other.money

    def __add__(self, other):
        """Redefines operator +."""

        if self.__class__.__name__ != other.__class__.__name__:
            total = self.money + other.to(locals()[self.__class__]).money
            return total
        else:
            total = self.money + other.money
            return total

    def __sub__(self, other):
        """Redefines operator -."""

        if self.__class__.__name__ != other.__class__.__name__:
            sub = self.money - other.to(globals()[self.__class__.__name__]).money
            return sub
        else:
            sub = self.money - other.amount
            return sub

    def __mul__(self, other):
        """Redefines operator *."""

        if isinstance(other, int) or isinstance(other, float):
            mul = self.money * other
            return mul
        else:
            raise TypeError('Please, use correct data.')

    def __div__(self, other):
        """Redefines operator /."""

        if isinstance(other, int) or isinstance(other, float):
            div = self.money / other
            return div
        else:
            raise TypeError('Please, use correct data.')

    def to(self, other):
        """Converts one currency to other currency."""

        return self.money * (self.value / other.value)

    @classmethod
    def course(cls, other):
        """Returns course.

        :param other: another currency.
        :type other: class.
        :returns: float c.
        """

        c = cls.value / other.value
        return c

    @property
    def _course(self):
        return globals()[self.__class__.__name__].value

    @_course.setter
    def _course(self, update):
        globals()[self.__class__.__name__].value = update
        return globals()[self.__class__.__name__].value


class Euro(Currency):
    """Class for Euro."""

    symbol = '€'
    currency = 'Euro'
    value = 73


class Dollar(Currency):
    """Class for Dollar."""

    symbol = chr(36)
    value = 64


class Rubble(Currency):
    """Class for Rubbles."""

    symbol = chr(8381)
    value = 1


if __name__ == '__main__':

    e = Euro(5)
    r = Rubble(10)
    print(r.to(Dollar))
    e = Euro(5)
    print(e)
    print(e * 2.5)
    print(e.to(Dollar))
    print(e > Euro(6))
    print(e.to(Rubble))