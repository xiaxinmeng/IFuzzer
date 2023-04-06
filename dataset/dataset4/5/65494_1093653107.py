import ast
tree = ast.parse("(sin\n(0.5))")
first_stmt = tree.body[0]
call = first_stmt.value
print("col_offset of call expression:", call.col_offset)
print("col_offset of func of the call:", call.func.col_offset)
print("lineno of call expression:", call.lineno)
print("lineno of func of the call:", call.lineno)