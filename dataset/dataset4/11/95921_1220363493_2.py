def f(a, b):
    if not b <= "A" == a:
        pass


import dis

for i in dis.get_instructions(f):
    print(i.positions, i.opname, i.argval)


f(1, 2)