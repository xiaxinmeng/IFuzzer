
import pyperf
runner = pyperf.Runner()
for n in [1,2,4,8,10,20,100]:
	runner.timeit(name=f"list({n}) repeat {1000}", stmt=f"x=a*{1000}", setup=f'a=list(range({n}))')
