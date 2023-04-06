
parameters = tuple(_type_check(p, msg) for p in parameters)
parameters = _remove_dups_flatten(parameters)
