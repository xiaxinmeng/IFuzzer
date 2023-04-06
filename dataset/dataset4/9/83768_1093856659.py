class HexInt(int):
    def __repr__(self):
        return hex(self)

class MyEnum(HexInt, enum.Enum):
    A = 1
    B = 2
    C = 3