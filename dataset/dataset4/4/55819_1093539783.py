class C(metaclass=ABCMeta):
    @MyProperty
    @abstractmethod
    def x(self):
        pass
    @x.setter
    @abstractmethod
    def x(self, val):
        pass