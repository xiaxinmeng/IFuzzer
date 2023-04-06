import dis

source = "def x(a, b): print(1)"
print(dis.Bytecode(source).dis())
print(dis.Bytecode(source).dis())
print(dis.Bytecode(source).dis() == dis.Bytecode(source).dis())