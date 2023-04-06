import ast

code = '''f"is {x:d}"'''
tree = ast.parse(code)

for n in ast.walk(tree):
    if isinstance(n, ast.FormattedValue):
        print(
            type(n.format_spec),
            len(n.format_spec.values),
            set(type(v) for v in n.format_spec.values),
        )