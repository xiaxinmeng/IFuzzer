class MyABC(abc.ABC):
    @abstractmethod
    def set_foo(self, v):
        pass
    @abstractmethod
    def reset_foo(self):
        pass