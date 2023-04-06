
import pyperf
runner = pyperf.Runner()
runner.timeit(name=f"x.insert(2, 1); x.pop(-1)",stmt='x.insert(2, 1); x.pop(1)', setup='x=[None]*1_00_000')
