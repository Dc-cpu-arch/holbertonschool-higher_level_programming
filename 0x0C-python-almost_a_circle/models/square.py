#!/usr/bin/python3
"""Subclass type Square from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Instantiation of a Square that inherits from a Rectangle Object"""

    def __init__(self, size, x=0, y=0, id=None):
        """Construction of the Object with its Private Attributes

        Args(from Rectangle):
        size (int): both width and height of Square
        x (int): X dimension of Square
        y (int): Y dimension of Square
        """
    super().__init__(size, size, x, y, id)

    """Get & Set decorators to set the size values to Square"""

    @property
    def size(self):
        """Gets the Size Attribute of Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the Size to width and height of Square"""
        self.width = value
        self.height = value

    """Displayment of basic information about Square"""

    def __str__(self):
        """Returns the basic information about Square's attributes"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.width)

    def to_dictionary(self):
        """Returns Square's attributes in dictionary form"""
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d

    """Object Attributes Update Modes"""

    def update(self, *args, **kwargs):
        """Updates the Squares' attributes wheter in the key-worded
            or in the no key-worded argument form"""
        if len(args):
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                if key == 1:
                    self.size = value
                if key == 2:
                    self.x = value
                else:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
