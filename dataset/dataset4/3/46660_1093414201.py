def _f(x=None):
   def g():
      x
   return g

CellType = type(_f().func_closure[0])