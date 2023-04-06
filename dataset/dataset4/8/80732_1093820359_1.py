import perf

runner = perf.Runner()
runner.timeit("list_comp",
               stmt="[x*2 for x in it]",
               setup="k=list(range(10));it=(x for x in k)")