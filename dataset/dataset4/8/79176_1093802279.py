class MyABC(abc.ABC):
    @abstractmethod
    def set_foo(self, v):
        pass
    reset_foo = partialmethod(set_foo, None)