def copy_lineno(node, new_node):
    ast.fix_missing_locations(new_node)
    ast.copy_location(new_node, node)
    return new_node