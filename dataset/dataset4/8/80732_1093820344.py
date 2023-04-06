import perf

runner = perf.Runner()
runner.timeit("list_comp",
               stmt="[x for x in range(10)]",
               setup="")