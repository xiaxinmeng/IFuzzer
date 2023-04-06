return bool(
  (isfunction(object) or ismethod(object)) and
   object.func_code.co_flags & CO_GENERATOR)