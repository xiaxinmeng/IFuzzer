def __getattr__(name):
  if name == 'unparse':
    import _ast_unparse
    globals()['unpase'] = _ast_unparse.unparse
    return _ast_unparse.unparse
  else:
    raise AttributeError