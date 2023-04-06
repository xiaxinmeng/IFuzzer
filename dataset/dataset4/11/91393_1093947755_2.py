class SomeProperty:
    @property
    def some_value(self) -> str: ...

class SomeClass(SomeProperty):
    def __init__(self, some_value):
        self.some_value = some_value

if __name__ == '__main__':
    a = SomeClass(some_value="value")