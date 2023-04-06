
class NiceObject:
    def __str__(self):
        return str(self.__dict__)
    def __repr__(self):
        return str(self)

s = NiceObject()
s.self = s
