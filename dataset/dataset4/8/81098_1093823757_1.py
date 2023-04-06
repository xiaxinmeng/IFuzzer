class V(ast.NodeVisitor):
    def visit_Str(self, node):
        ...

    def visit_Bytes(self, node):
        ...

    def visit_Num(self, node):
        ...

    def visit_Constant(self, node):
        if isinstance(node.value, str):
             return self.visit_Str(node)
        # Annoying special case, bools are ints, before this wouldn't call
        # `visit_Num` because there was a separate `visit_NameConstant` for `True` / `False`
        elif isinstance(node.value, int) and not isinstance(node.value, bool):
            return self.visit_Num(node)
        elif isinstance(node.value, bytes):
            return self.visit_Bytes(node)
        else:
            return self.generic_visit(node)