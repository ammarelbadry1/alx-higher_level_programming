#!/usr/bin/python3
"""8-base_geometry Module

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
            value (int): the integer to bev checked.
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
