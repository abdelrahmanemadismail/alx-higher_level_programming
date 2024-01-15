#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the Square instance"""
        s = "[Square] ({}) {}/{} - {}"
        return s.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes with positional and keyword arguments"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
