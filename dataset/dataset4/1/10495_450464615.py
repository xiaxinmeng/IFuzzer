
import perf

runner = perf.Runner()

runner.timeit("namedtuple",
        stmt="a.x",
        setup="""\
import collections
a = collections.namedtuple('A', ['x'])(3)
""")

runner.timeit("slots",
        stmt="b.x",
        setup="""\
class B:
    __slots__ = ("x",)

    def __init__(self, x):
        self.x = x
b = B(3)
""")

runner.timeit("tuple",
        stmt="b[0]",
        setup="""\
b = (3,)
""")
