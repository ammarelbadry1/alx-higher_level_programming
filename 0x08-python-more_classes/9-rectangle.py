#!/usr/bin/python3

"""Define a class Rectangle."""


class Rectangle:
    """Rectangle objects standard."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """New rectangle constructor.

        Args:
            width (int): the width of the created rectangle.
            height (int): the height of the created rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """Rectangle objects destructor."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

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

    def __str__(self):
        """Formatted representation of the current object."""
        my_str = ""
        if (self.__width == 0 or self.__height == 0):
            return my_str
        for i in range(self.__height):
            for j in range(self.__width):
                my_str += str(self.print_symbol)
            if (i != self.__height - 1):
                my_str += "\n"
        return my_str

    def __repr__(self):
        """String representation of the current object."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare between two Rectangle instances.

        Args:
            rect_1 (object): first rectangle object.
            rect_2 (object): second rectangle object.
        """
        if (not isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (not isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if (area_1 == area_2 or area_1 > area_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a square."""
        return cls(size, size)
