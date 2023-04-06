import pyperf

runner = pyperf.Runner()
runner.timeit(name="frozenset create test",
              stmt="frozenset([1, 2, 3, 4, 5])")
