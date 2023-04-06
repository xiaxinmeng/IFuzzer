def _cmp_fn(name, op, self_tuple, other_tuple):
    return _recursive_eq(_create_fn(name,
                      ('self', 'other'),
                      [ 'if other.__class__ is self.__class__:',
                       f' return {self_tuple}{op}{other_tuple}',
                        'return NotImplemented']))