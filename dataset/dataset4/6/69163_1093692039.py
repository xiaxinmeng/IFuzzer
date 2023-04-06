code = '''                                                                     
a = { 'x':1, 'y':2 }
b = { **a, 'z': 3 }
'''

# Works
ccode = compile(code, '', 'exec')

# Crashes
import ast
tree = ast.parse(code)
ccode = compile(tree, '', 'exec')