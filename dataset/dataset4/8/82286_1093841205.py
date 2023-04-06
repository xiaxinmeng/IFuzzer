class C:
    def __init__(self, x, h):
        self.x = x
        self.h = h

    def __eq__(self, other):
        print(f"{self}.__eq__({other})")
        return self.x == other.x

    def __hash__(self):
        print(f"{self}.__hash__")
        return self.h

    def __repr__(self):
        return f"C({self.x, self.h})"