
import dis, abc
import ast as art
dix = dis
ast = art

def f():
    dix.a()  # Is first name affected if not bound name? (No.)
    dis.a()  # Is bound-file name affected if not first? (Yes.)
    abc.a()  # Are names other than 'dis' affected?  (Yes.)
    art.a()  # Is bound name not file name affected? (Yes.)
    ast.a()  # Is file name not bound name affected?  (No.)

for i in dis.Bytecode(f):
    if i.opname == "LOAD_GLOBAL":
        print(f'{i.opname:12s}', i.positions)
