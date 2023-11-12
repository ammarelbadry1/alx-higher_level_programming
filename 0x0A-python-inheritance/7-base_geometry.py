#!/usr/bin/python3
"""5-base_geometry Module

Defines an empty class BaseGeometry.
"""


class BaseGeometry:
    """Represent class BaseGeometry."""
    pass

    def area(self):
        """Calculates geometry area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check and validate integer.
        
        Args:
            name (str): the name to be checked.
            value (int): the integer to be checked.
        """
        if (not isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
