@enum.unique
class Color(enum.Enum):
    red = 1
    blue = 2
    green = 3

@enum.unique
class Shape(enum.Enum):
    """Member values denote number of sides."""
    circle = 1
    triangle = 3
    square = 4