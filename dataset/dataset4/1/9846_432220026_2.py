import perf

runner = perf.Runner()
runner.timeit("list(x)",
              stmt="list(x)",
              setup="x = [0]*10000")