def f(a, b):
    if a != b and b <= "A" == a:
        pass


import dis

for i in dis.get_instructions(f):
    print(i.positions, i.opname, i.argval)


f(1, 2)