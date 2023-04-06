
class Sub:
    pass

class Base:
    _sub: list[Sub]

class Sub:
    _parent: Base
