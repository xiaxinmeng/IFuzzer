class Animal(metaclass=ABCMeta):
    pass

class Plant(metaclass=ABCMeta):
    def __init_subclass__(cls):
        assert not issubclass(cls, Animal), "Plants cannot be Animals"

class Dog(Animal):
    pass