class Spam(int):
    def __new__(cls, value):
        self = super().__new__(Spam, value)
        self._eggs = 10
        return self