#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle():
    """Represent a Rectangle"""

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
        """Get the width of the rectangle."""
        return self.__width

    @property
    """Get the height of the rectangle."""
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
