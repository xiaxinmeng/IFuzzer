
import dis
dix = dis
dum = 5
def f(): dis, dix, dum

for i in dis.Bytecode(f):
    if i.opname == "LOAD_GLOBAL":
        print(i.positions)
