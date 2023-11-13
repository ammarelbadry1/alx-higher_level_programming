#!/usr/bin/python3
"""9-base_geometry Module

Defines a class BaseGeometry.
"""


class BaseGeometry:
    """Represent class BaseGeometry."""

    def area(self):
        """Calculates geometry area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check and validate integer.

        Args:
            name (str): the name to be checked.
            value (int): the integer to be checked.
        """
        if (value.__class__.__name__ != int.__name__):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represent class Rectangle generalized to BaseGeometry class."""

    def __init__(self, width, height):
        """Initialize a new Rectangle

        Args:
            width (int): The width of the created rectangle
            height (int): The height of the created rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of a created Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Print the class in user friendly way."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Represent class Square generalized to Rectangle class."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the created square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Print the class in user friendly way."""
        return "[Square] {}/{}".format(self.__size, self.__size)
