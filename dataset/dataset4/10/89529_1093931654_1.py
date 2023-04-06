
from dataclasses import dataclass, field

@dataclass(init=False)
class TestObject(object):
    m: str = field(default='hi')
    k: list = field(default_factory=list)

    def test(self):
        print(f'm is {self.m} ')
        self.k.append(1)
        print(f'k is {self.k}')

if __name__ == '__main__':
    myobject = TestObject()
    print(TestObject.m)  # hi
    print(TestObject.k)  # []

    myobject.test()
    # m is hi 
    # k is [1]

    other_object = TestObject()
    other_object.test()
    # m is hi 
    # k is [1, 1]
