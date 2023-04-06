def callable(obj):
  return any("__call__" in klass.__dict__ for klass in type(obj).__mro__)