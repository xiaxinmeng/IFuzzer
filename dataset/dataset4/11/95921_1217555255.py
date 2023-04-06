def f(s):
    return (s if (0 < s < 256) else "?")

import dis

for i in dis.get_instructions(f):
    print(i.positions, i.opname, i.argval)

f("abc")