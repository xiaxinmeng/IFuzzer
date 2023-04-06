
import pyperf
runner = pyperf.Runner()

setup='l=[1,2,None,4,5,6,7,8,9,10]; t=(1,None,3,4)'

runner.timeit(name=f"list", stmt=f"x=l[3]",setup=setup)
runner.timeit(name=f"tuple", stmt=f"x=t[2]",setup=setup)
code="""
for ii in range(400):
	idx=ii%4
	a=l[idx]
	b=t[idx]	
"""
runner.timeit(name=f"mixed", stmt=code,setup=setup)

code="""
a=[ [1,2,3,4], (1,2,None)] * 100
for seq in a:
	value = seq[1]
"""
runner.timeit(name=f"mixed_same_opcode", stmt=code,setup=setup)
