class odict(dict):

   def __init__(self, d={}):
      self._keys = d.keys()
      dict.__init__(self, d)

   def __setitem__(self, key, item):
        dict.__setitem__(self, key, item)
        if key not in self._keys:
            self._keys.append(key)