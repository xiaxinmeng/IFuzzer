import ast


tree_1 = ast.parse("A[1:2, *l]")
tree_2 = ast.parse(ast.unparse(tree_1))
assert ast.dump(tree_1) == ast.dump(tree_2)