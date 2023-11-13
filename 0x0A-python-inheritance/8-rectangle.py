#!/usr/bin/python3
"""8-base_geometry Module

Defines a class BaseGeometry.
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


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
