import ast
mylist = []
n = 100000
print(ast.parse("mylist"+"+mylist"*n))