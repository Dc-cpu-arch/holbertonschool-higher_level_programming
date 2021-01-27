#!/usr/bin/python3
"""Subclass type Rectangle from Base"""

from models.base import Base


class Rectangle(Base):
    """Instantiation of a Rectangle Object from Base Parent"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Construction of the Object with its Private Attributes

        Args:
        width (int): Rectangle width
        height (int): Rectangle height
        x (int, optional): X dimension of Rectangle (default is 0)
        y (int, optional): Y dimension of Rectangle (default is 0)
        id (int, optional): Rectangle id (default is None)
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        """Get & Set decorators to filter Types and Values of attributes"""

    @property
    def width(self):
        """Gets the Private Attribute of Rectangle"""
        return self.__width

    @property
    def height(self):
        """Gets the Private Attribute of Rectangle"""
        return self.__height

    @property
    def x(self):
        """Gets the Private Attribute of Rectangle"""
        return self.__x

    @property
    def y(self):
        """Gets the Private Attribute of Rectangle"""
        return self.__y

    @width.setter
    def width(self, value):
        """Assigns value to attribute

        Raises:
        TypeError: if value is not integer
        ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Assigns value to attribute

        Raises:
        TypeError: if value is not integer
        ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Assigns value to attribute

        Raises:
        TypeError: if value is not integer
        ValueError: if vale is < 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Assigns value to attribute

        Raises:
        TypeError: if value is not integer
        ValueError: if value is < 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """Displayment of attributes of Rectangle"""

    def area(self):
        """Rectangle method to calculate its area"""
        return self.__width * self__height

    def display(self):
        """Prints the object with the '#' character in STDOUT"""
        print("\n" * self.__y +
              "\n".join(" " * self.__x + "#" * self.__width
                        for i in range(self.__height)))

    def __str__(self):
        """Returns the basic attributes from Rectangle"""
        return ("[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def to_dictionary(self):
        """Returns Rectangle's attributes in dictionary form"""
        d={}
        d["id"]=self.id
        d["width"]=self.width
        d["height"]=self.height
        d["x"]=self.x
        d["y"]=self.y
        return d

    """Object Attributes Update Modes"""

    def update(self, *args, **kwargs):
        """Updates the values of Rectangle's attributes wheter
        in the key-worded or in the no key-worded argument form
        """
        if args:
            for key, value in enumerate(args):
                if key == 0:
                    self.id=value
                elif key == 1:
                    self.width=value
                elif key == 2:
                    self.height=value
                elif key == 3:
                    self.x=value
                else:
                    self.y=value
        else:
            if "id" in kwargs:
                self.id=kwargs["id"]
            if "width" in kwargs:
                self.width=kwargs["width"]
            if "height" in kwargs:
                self.height=kwargs["height"]
            if "x" in kwargs:
                self.x=kwargs["x"]
            if "y" in kwargs:
                self.y=kwargs["y"]
