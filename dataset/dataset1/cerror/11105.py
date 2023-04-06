import ast
e = ast.UnaryOp(op=ast.Not(), lineno=0, col_offset=0)
e.operand = e
compile(ast.Expression(e), "<test>", "eval")
