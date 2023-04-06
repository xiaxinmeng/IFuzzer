class mydict(dict):
    def __setitem__(self, name, value):
        if name == "__module__":
            value = "<mock module>"
        super().__setitem__(name, value)

class MetaClass(type):
    @classmethod
    def __prepare__(mcl, name, bases):
        return mydict()

class A(metaclass=MetaClass):
    pass

print(A.__module__)