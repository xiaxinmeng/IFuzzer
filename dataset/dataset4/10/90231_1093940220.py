
def get_type_comment(self, node):
    comment = self._type_ignores.get(node.lineno) if hasattr(node, "lineno") else node.type_comment
    if comment is not None:
        return f" # type: {comment}"
