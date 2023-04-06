for node in ast.walk(root_node):
    if isinstance(node, ast.ImportFrom) and node.module == '__future__':
        node.module = '__future__'