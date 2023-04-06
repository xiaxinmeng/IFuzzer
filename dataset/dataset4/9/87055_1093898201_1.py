print("new code:","------------")
print(ast.unparse(newast))
print("------------")

c = compile(newast,'','exec')
exec(c)