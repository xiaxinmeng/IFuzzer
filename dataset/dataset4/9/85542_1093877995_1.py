def _eval_type(t, globalns, localns, recursive_guard=frozenset()):
    if isinstance(t, str):
        t = ForwardRef(t)
    if isinstance(t, ForwardRef):
       ...