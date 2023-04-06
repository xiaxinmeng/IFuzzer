class Temperature(metaclass=ABCMeta):
    @abc.abstractclassmethod
    def from_fahrenheit(self, t):
        ...
    @abc.abstractclassmethod
    def from_celsius(self, t):
        ...