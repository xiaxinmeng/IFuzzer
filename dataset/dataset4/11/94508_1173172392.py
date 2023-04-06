
import pyperf

runner = pyperf.Runner()

for n in [1, 2, 10, 100, 1000, 50_000]:
    runner.timeit(name=f"list({n}).insert(0, None)",
	      stmt="lst.insert(0, None)", setup=f'import random; lst=[random.random() for ii in range({n})]')
    runner.timeit(name=f"list({n}).slice",
	      stmt="lst[:0] = [None]", setup=f'import random; lst=[random.random() for ii in range({n})]')
