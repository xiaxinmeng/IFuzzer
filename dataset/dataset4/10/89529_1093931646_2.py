from dataclasses import dataclass, field

@dataclass(init=False)
class TestObject(object):
    m: str = field(default='hi')
    k: list = field(default_factory=list)

    def test(self):
        print(f'm is {self.m} ')
        print(f'k is {self.k}')


@dataclass
class InheritedTestObject(TestObject):

    def __post_init__(self):
        super().__init__()
        print(f'Inherited m is {self.m} ')
        print(f'Inherited k is {self.k}')
        print(f'Inherited g is {self.k}')


if __name__ == '__main__':
    myobject = InheritedTestObject()
    myobject.test()