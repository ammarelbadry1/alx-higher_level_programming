#!/usr/bin/python3
"""square Module

This module represents a class Square.
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Define a class Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square

        Args:
            size (int): The size of the Square created
            x (int): The offset of the Square created
            y (int): The offset of the Square created
            id (int): The id of the Square created
        """

        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Get/Set the size attribute of the current object."""
        return self.__size

    @size.setter
    def size(self, size):
        if (not isinstance(size, int)):
            raise TypeError("width must be an integer")
        if (size <= 0):
            raise ValueError("width must be > 0")
        self.__size = size

    def __str__(self):
        """Print the Square instance in a user friendly way."""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute of the Square instance.

        Args:
            args (tuple): variable length list of arguments.
            kwargs (dict): variable length dictionary of key-value pairs.
        """

        if (args):
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            if ("id" in kwargs):
                self.id = kwargs["id"]
            if ("size" in kwargs):
                self.size = kwargs["size"]
            if ("x" in kwargs):
                self.x = kwargs["x"]
            if ("y" in kwargs):
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        object_dict = {
                        "id": self.id,
                        "x": self.x,
                        "size": self.size,
                        "y": self.y
                      }
        return object_dict
