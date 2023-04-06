import ast
code = '''
import itertools as it
class a(it.count):
    def __init__(self, n): pass
    def extra(self, m:int) -> int: pass
'''
tree = ast.parse(code)
for node in ast.walk(tree):  
    print(node)  # This produces same as ast.dump(tree)
    print(node._fields)