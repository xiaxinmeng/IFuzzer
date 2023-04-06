class MagicMockChild(MagicMock):
    def __init__(self):
        super().__init__()
        self.__len__ = lambda self : 9