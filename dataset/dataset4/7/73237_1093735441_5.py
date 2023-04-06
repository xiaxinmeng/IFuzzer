import ast

code = '''
f'{LOL}'
'''

for node in ast.walk(ast.parse(code, "<stdin>", "exec")):
    if isinstance(node, ast.Name):
        print(node.lineno)