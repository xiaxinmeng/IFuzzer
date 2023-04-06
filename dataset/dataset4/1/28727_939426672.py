from pyperf import Runner

runner = Runner()

runner.timeit(
    "int: x*x",
    setup="from itertools import repeat; it = repeat(1, 1_000_000)",
    stmt="for x in it: x*x")

runner.timeit(
    "float: x*x",
    setup="from itertools import repeat; it = repeat(1.0, 1_000_000)",
    stmt="for x in it: x*x")

runner.timeit(
    "int: x*...*x",
    setup="from itertools import repeat; it = repeat(1, 1_000_000)",
    stmt="for x in it: x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x")

runner.timeit(
    "float: x*...*x",
    setup="from itertools import repeat; it = repeat(1.0, 1_000_000)",
    stmt="for x in it: x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x")