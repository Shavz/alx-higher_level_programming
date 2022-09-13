#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """Represents a square"""
    
    def __init__(self, size=0):
        """initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    def area(self):
        """calculates the square's area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """get the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, other):
        """Compare if square is less than another by area"""
        return self.size < other.size

    def __le__(self, other):
        """Compare if square is less than or equal to another by area"""
        return self.size <= other.size

    def __eq__(self, other):
        """Compare if square is equal to another by area"""
        return self.size == other.size

    def __ne__(self, other):
        """Compare if square is not equal to another by area"""
        return self.size != other.size

    def __ge__(self, other):
        """Compare if square is greater than or equal to another by area"""
        return self.size >= other.size

    def __gt__(self, other):
        """Compare if square is greater than another by area"""
        return self.size > other.size
