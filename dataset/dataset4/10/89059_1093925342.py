
#!/usr/bin/env python3
import ast
import sys

print(sys.version)

good = ast.Assign(
    targets=[ast.Name(id="hello", ctx=ast.Store())],
    value=ast.Constant(value="world"),
    lineno=1
)
print(ast.unparse(good))


bad = ast.Assign(
    targets=[ast.Name(id="hello", ctx=ast.Store())],
    value=ast.Constant(value="world"),
)
print(ast.unparse(bad))
