import ast

tree = ast.BinOp(left=ast.Num(n=2), right=ast.Num(n=2), op=ast.Add())
expr = ast.Expression(body=[tree])
ast.fix_missing_locations(expr)
exe = compile(expr, filename="", mode="eval")
print(eval(exe))