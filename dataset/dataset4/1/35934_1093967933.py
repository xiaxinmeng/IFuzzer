class mydict(dict):
   def popitem( self, key=None ):
        if key is None:  return dict.popitem(self)
        value = self[key]
        del self[key]
        return (key, value)