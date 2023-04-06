class Coordinate(metaclass=MyType):
    x: float
    y: float

class Address(metaclass=MyType):
    street: str
    country: str


class Location(Address, Coordinate):
    pass


class Location2(Address, Coordinate):
    name: str


print(Location.__annotations__)
print(Location2.__annotations__)