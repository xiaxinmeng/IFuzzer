def f(a,b):
    if a is b is None:
        return 5

import dis

for i in dis.get_instructions(f):
    print(i.positions, i.opname, i.argval)


f(1,2)