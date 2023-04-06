def string_nodes_are_eqivalent(node1, node2):
  if is_f_string(node1) and is_f_string(node2):
    # This would require to parse the nodes using ast.parse
    return f_strings_are_equivalent(node1, node2)
  if not is_f_string(node1) and not is_f_string(node2):
    return ast.literal_eval(node1.value) == ast.literal_eval(node2.value)
  return False