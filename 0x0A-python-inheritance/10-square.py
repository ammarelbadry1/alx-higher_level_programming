#!/usr/bin/python3
"""9-base_geometry Module

Defines a class BaseGeometry.
"""


Rectangle = __import__("9-rectangle").Rectangle


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
