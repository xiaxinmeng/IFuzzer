
# AST types of nodes that cannot be removed
_CANNOT_REMOVE_TYPES = (ast.Global, ast.Nonlocal, ast.Yield, ast.YieldFrom,
                        # don't remove 'except' block if it contains continue
                        # or break: see can_move_final() for the rationale
                        ast.Continue)

_CANNOT_MOVE_FINAL = (ast.Continue,)
