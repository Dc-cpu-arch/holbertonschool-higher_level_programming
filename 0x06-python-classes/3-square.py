#!/usr/bin/python3
"""Class Square representation in Python Code"""


class Square:
    """An instantiation of class Square

    Attributes:
        __size: size of every side of the square
        private attribute
    """

    def __init__(self, size=0):
        """Initialization method of a square

        Args:
            size: integer type to be assigned to __size

        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """Method to calculate square's area

        Args:
            __size

        Returns:
            Square's area
        """
        return self.size * self._size
