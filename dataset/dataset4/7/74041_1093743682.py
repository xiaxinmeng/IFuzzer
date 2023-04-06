class Property:
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, cls):
        return self.getter(cls if instance is None else instance)

class MyClass:
    @Property
    def something(cls):
        return cls.something