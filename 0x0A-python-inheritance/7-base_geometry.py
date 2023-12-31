#!/usr/bin/python3
"""7-base_geometry Module

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
