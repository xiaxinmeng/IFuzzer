import ast

code = "f(" + ",".join(['a' for _ in range(100000)]) + ")"
print("Ready!")
ast.parse(code)