import ast
t = ast.fix_missing_locations(ast.Expression(ast.Name("True", ast.Load())))
compile(t, "<t>", "eval")