from dataclasses import dataclass, field

@dataclass(init=False)
class TestObject(object):
    m: str = field(default='hi')
    k: list = field(init=False, default_factory=list)

    def test(self):
        print(f'm is {self.m} ')
        print(f'k is {self.k}')

if __name__ == '__main__':
    myobject = TestObject()
    myobject.test()