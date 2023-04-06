import perf

runner = perf.Runner()
runner.timeit("list_comp",
               stmt="[x**2 for x in k]",
               setup="k=iter(list(range(10)))")