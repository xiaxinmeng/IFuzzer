import abc


class Base(abc.ABC):
    def __init_subclass__(cls, **kwargs):
        instance = cls()
        print(f"Created instance of {cls} easily: {instance}")


    @abc.abstractmethod
    def do_something(self):
        pass


class Derived(Base):
    pass