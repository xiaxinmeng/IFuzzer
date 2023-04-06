class V(ast.NodeVisitor):
    def _visit_string(self, node, value):
        ...

    def visit_Str(self, node):
        return self._visit_string(node, node.s)

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            return self._visit_string(node, node.value)
        ...