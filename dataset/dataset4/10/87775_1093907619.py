fun1 = ast.FunctionType(
    argtypes=[],
    returns=ast.BinOp(
        left=ast.Name(id='int'),
        op=ast.BitOr(),
        right=ast.Name(id='float'),
    )
)
fun2 = ast.BinOp(
    left=ast.FunctionType(
        argtypes=[],
        returns=ast.Name(id='int'),
    ),
    op=ast.BitOr(),
    right=ast.Name(id='float'),
)