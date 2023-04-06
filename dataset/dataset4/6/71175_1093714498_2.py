@enum.unique
class Color(enum.Enum):
    aquamarine = 1
    blue = 2
    fushia = 3
    # inserting a member here (perhaps because it's clearest to keep these in alphabetic order)
    # results in having to increment all following members
    ...
    green = 40
    red = 41