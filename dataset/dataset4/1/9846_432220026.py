import perf

runner = perf.Runner()
runner.timeit("list(x)",
              stmt="list(x)",
              setup="x = iter(list(range(10)))")