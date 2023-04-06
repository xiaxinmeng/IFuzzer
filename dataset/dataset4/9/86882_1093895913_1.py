import ast
mylist = []
n = 1000000
print(ast.parse("mylist"+"+mylist"*n))
# <_ast.Module object at 0x7f78d7b672e8>