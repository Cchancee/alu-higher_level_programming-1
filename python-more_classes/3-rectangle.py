#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initiation of a new Rectangle
        :param width: The width of the initiated rectangle
        :type width: int
        :param height: The height of the initiated rectangle
        :typr height: int
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle"""
        return self.__width * self.height

    def perimeter(self):
        """Return the perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
    def __str__(self):
        """Return # representation of reactangle"""
        if self.__width == 0 or self.__height == 0:
            return
        str_ = []
        for i in range(self.__height):
            # print("#" * self.__width)
            [str_.append("#" for j in range(self.__width))]
            if i != self.__height -1:
                str_.append("\n")
        return ("".join(str_))
