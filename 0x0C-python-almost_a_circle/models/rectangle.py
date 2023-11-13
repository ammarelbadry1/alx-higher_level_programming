#!/usr/bin/python3
"""rectangle Module

This module represent a class Rectangle.
"""
from .base import Base


class Rectangle(Base):
    """Define a class Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance

        Args:
            width (int): the width of the Rectangle instance created
            height (int): the height of the Rectangle instance created
            x (int): the x offset of the Rectangle instance created
            y (int): the y offset of the Rectangle instance created
            id (int): the id of the Rectangle instance created
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get/Set the width attribute of the current object."""
        return self.__width

    @width.setter
    def width(self, width):
        if (not isinstance(width, int)):
            raise TypeError("width must be an integer")
        if (width <= 0):
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Get/Set the height attribute of the current object."""
        return self.__height

    @height.setter
    def height(self, height):
        if (not isinstance(height, int)):
            raise TypeError("height must be an integer")
        if (height <= 0):
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Get/Set the x attribute of the current object."""
        return self.__x

    @x.setter
    def x(self, x):
        if (not isinstance(x, int)):
            raise TypeError("x must be an integer")
        if (x < 0):
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Get/Set the y attribute of the current object."""
        return self.__y

    @y.setter
    def y(self, y):
        if (not isinstance(y, int)):
            raise TypeError("y must be an integer")
        if (y < 0):
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculates the area a Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle instance with the character #."""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Print the Rectangle instance in a user friendly way."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute of the Rectangle instance.

        Args:
            args (tuple): variable length list of arguments.
            kwargs (dict): variable length dictionary of key-value pairs.
        """

        if (args):
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            if ("id" in kwargs):
                self.id = kwargs["id"]
            if ("width" in kwargs):
                self.width = kwargs["width"]
            if ("height" in kwargs):
                self.height = kwargs["height"]
            if ("x" in kwargs):
                self.x = kwargs["x"]
            if ("y" in kwargs):
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        object_dict = {
                        "x": self.x,
                        "y": self.y,
                        "id": self.id,
                        "height": self.height,
                        "width": self.width
                      }
        return object_dict
