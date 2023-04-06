class X(int):
    def __hash__(self):
        print('hash', self)
        return int.__hash__(self)