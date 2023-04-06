class AttrDict(dict):
   def __init__(self, *args, **kw):
      dict.__init__(self, *args, **kw)
   
   def __getattr__(self, key):
      return self[key]
   
   def __setattr__(self, key, value):
      self[key] = value