#!/usr/bin/python3

"""Define a class Rectangle."""


class Rectangle:
    """Rectangle objects standard."""

    def __init__(self, width=0, height=0):
        """New rectangle constructor.

        Args:
            width (int): the width of the created rectangle.
            height (int): the height of the created rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/Set the width attribute of the current object."""
        return (self.__width)

    @width.setter
    def width(self, width):
        if (not isinstance(width, int)):
            raise TypeError("width must be an integer")
        if (width < 0):
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Get/Set the height attribute of the current object."""
        return (self.__height)

    @height.setter
    def height(self, height):
        if (not isinstance(height, int)):
            raise TypeError("height must be an integer")
        if (height < 0):
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Calculates the object area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the object perimeter."""
        if (self.__width == 0 or self.height == 0):
            return 0
        return (2 * (self.__width + self.__height))
