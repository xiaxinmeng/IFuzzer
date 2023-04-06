import enum
class Color(enum.Flag):
    RED = enum.auto()
    BLUE = enum.auto()
    GREEN = enum.auto()

white = Color.RED | Color.BLUE | Color.GREEN
assert white.name is None