from pyperf import Runner

runner = Runner()

runner.timeit("int+=int",
    setup="from itertools import repeat",
    stmt="x = 0\n"
         "for y in repeat(1, 10_000):\n"
         "    x += y; x += y; x += y; x += y; x += y"
    )
runner.timeit("float+=float",
    setup="from itertools import repeat",
    stmt="x = 0.0\n"
         "for y in repeat(1.0, 10_000):\n"
         "    x += y; x += y; x += y; x += y; x += y"
    )
runner.timeit("str+=str",
    setup="from itertools import repeat",
    stmt="for y in repeat('a', 10_000):\n"
         "    x = ''; x += y; x += y; x += y; x += y; x += y"
    )
runner.timeit("list[0]+=str",
    setup="from itertools import repeat",
    stmt="x = [None]\n"
         "for y in repeat('a', 10_000):\n"
         "    x[0] = ''; x[0] += y; x[0] += y; x[0] += y; x[0] += y; x[0] += y"
    )
runner.timeit("float+=int",
    setup="from itertools import repeat",
    stmt="x = 0.0\n"
         "for y in repeat(1, 10_000):\n"
         "    x += y; x += y; x += y; x += y; x += y"
    )
runner.timeit("decimal+=decimal",
    setup="from itertools import repeat; from decimal import Decimal as D",
    stmt="x = D(0)\n"
         "for y in repeat(D(1), 10_000):\n"
         "    x += y; x += y; x += y; x += y; x += y"
    )
runner.timeit("list[0]+=1",
    setup="from itertools import repeat; from collections import defaultdict",
    stmt="dd = [0]\n"
         "for y in repeat(1, 10_000):\n"
         "    dd[0] += y; dd[0] += y; dd[0] += y; dd[0] += y; dd[0] += y",
    )
runner.timeit("defaultdict(int)[0]+=1",
    setup="from itertools import repeat; from collections import defaultdict",
    stmt="dd = defaultdict(int)\n"
         "for y in repeat(1, 10_000):\n"
         "    dd[0] += y; dd[0] += y; dd[0] += y; dd[0] += y; dd[0] += y",
    )