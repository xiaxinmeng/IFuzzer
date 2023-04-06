def type_call(type, *args, **kws):
   r = type.__new__(type, *args, **kws)
   if not issubclass(r, type):
       type(r).__init__(r, *args, **kws)
   return r