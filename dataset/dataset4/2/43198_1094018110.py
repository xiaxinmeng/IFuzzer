class AttrDict(dict):
   def __init__(self, *args, **kw):
      dict.__init__(self, *args, **kw)
      self.__dict__ = self