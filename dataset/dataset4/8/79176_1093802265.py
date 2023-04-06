class MyABC(metaclass=ABCMeta):
    @property
    @abstractmethod
    def myprop(self):
        ...

class MyConcrete(MyABC):
    @cached_property
    def myprop(self):
        return self._some_heavy_work()