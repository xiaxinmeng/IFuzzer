from enum import Flag, auto


class FlagIter(Flag):
    def __iter__(self):
        for memeber in self._member_map_.values():
            if member in self:
                yield member


class Colour(FlagIter):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    YELLOW = RED | GREEN

cyan = Colour.GREEN | Colour.Blue

print(*Colour)  # Colour.RED Colour.GREEN Colour.BLUE Colour.YELLOW

# Without the enhancement, 'not iterable' is thrown for these
print(*cyan)  # Colour.GREEN Colour.BLUE
print(*Colour.YELLOW)  # Colour.RED Colour.GREEN Colour.YELLOW
print(*~Colour.RED)  # Colour.GREEN Colour.BLUE