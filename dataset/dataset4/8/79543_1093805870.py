class Test(list, metaclass=ABCMeta):
    @abstractmethod
    def test(self):
        pass
test = Test()