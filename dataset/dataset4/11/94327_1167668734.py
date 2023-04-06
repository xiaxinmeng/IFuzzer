import timeit


class Base:
    def __init__(self, a):
        self.a = a


class Super(Base):
    def __init__(self, a):
        super().__init__(a)


class Direct(Base):
    def __init__(self, a):
        Base.__init__(self, a)



print(timeit.timeit('Super(1)', "from __main__ import Super", number=100000))
# 0.03609574999427423
print(timeit.timeit('Direct(1)', "from __main__ import Direct", number=100000))
# 0.024121000024024397