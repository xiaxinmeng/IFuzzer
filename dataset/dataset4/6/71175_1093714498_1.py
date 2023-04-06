class Color(enum.AutoNumberedEnum):
    red = ()
    blue = ()
    green = ()

@enum.unique
class Shape(enum.Enum):
    """Member values denote number of sides."""
    circle = 1
    triangle = 3
    square = 4