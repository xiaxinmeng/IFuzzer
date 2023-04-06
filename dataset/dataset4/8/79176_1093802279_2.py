class MyABC(abc.ABC):
    @abstractmethod
    def set_foo(self, v):
        pass

    # No need to override if default implementation is OK
    def reset_foo(self):
        self.set_foo(None)