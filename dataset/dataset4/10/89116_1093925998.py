from operator import itemgetter, attrgetter
from pyperf import Runner

class MyClass:
    __slots__ = "a", "b"

namespace = {'itemgetter': itemgetter,
             'attrgetter': attrgetter,
             'MyClass': MyClass,
             }

runner = Runner()
runner.timeit(
    name="itemgetter",
    setup="f = itemgetter(1); x = (1, 2, 3)",
    stmt="f(x)",
    globals=namespace
)
runner.timeit(
    name="attrgetter",
    setup="f = attrgetter('b'); x = MyClass(); x.a = x.b = 1",
    stmt="f(x)",
    globals=namespace
)