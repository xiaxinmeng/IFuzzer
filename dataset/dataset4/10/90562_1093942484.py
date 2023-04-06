
from attrs import define


@define
class A:
    pass


@define
class B(A):
    def test(self):
        super()


B().test()
