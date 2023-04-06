class V(ast.NodeVisitor):
    def visit_Str(self, node):
        ...

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            self.visit_Str(node)
        else:
            self.generic_visit(node)