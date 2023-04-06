class BaseClass(ABC):
    pass


class MyDerivedClass(BaseClass):

    def __init__(self, thing):
        self.thing = thing

thing = MyDerivedClass()