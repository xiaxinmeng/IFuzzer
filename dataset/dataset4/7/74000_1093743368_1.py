
#!/usr/bin/env python3.6

import ast

code1 = '''"\\{x}"'''
code2 = '''f"\\{x}"'''

tree1 = ast.parse(code1, mode='eval')
print(ast.dump(tree1))
tree2 = ast.parse(code2, mode='eval')
print(ast.dump(tree2))
