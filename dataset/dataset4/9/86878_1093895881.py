import ast
mylist = []
n = 1000000
print(ast.literal_eval("mylist"+"+mylist"*n))