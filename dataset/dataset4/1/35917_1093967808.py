class meta1(type):
    def __new__(tp, name, bases, attr):
        return type.__new__(tp, name, bases, attr)

class meta2(type):
    pass