from pyperf import Runner

runner = Runner()

for n in [10, 100, 1000, 10_000, 100_000]:
    runner.timeit(f"for i in range({n}): pass",
                stmt=f"for i in range({n}): pass")