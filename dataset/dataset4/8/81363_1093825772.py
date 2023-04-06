import ast

txt1 = '"""\\n"""'
txt2 = '"""\n"""'

tree1 = ast.parse(txt1)
tree2 = ast.parse(txt2)

print(tree1.body[0].value.s == tree2.body[0].value.s)
print(bytes(tree1.body[0].value.s, encoding='utf-8'))
print(bytes(tree2.body[0].value.s, encoding='utf-8'))