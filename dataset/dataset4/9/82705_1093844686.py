
from functools import cached_property
def age(self):
    return 10
class A:
    def __init__(self):
        setattr(self.__class__, 'age', property(age))
        setattr(self.__class__, 'age3', cached_property(age))

    age2 = cached_property(age)

a = A()
print(a.age)    # 10
print(a.age2)   # 10
print(a.age3)   # TypeError: Cannot use cached_property instance without calling __set_name__
