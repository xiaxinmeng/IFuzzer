class MyLib():
  def __init__(arg1, arg2):
    self._cacheSize = someComputation(arg1, arg2) # returns a number
  @lru_cache
  def foo_long(self, arg1, **kwds):
    pass
#user
import MyLib 
i = MyLib(100, 21)
# not to make it so simple: 
i.changeInternalStateSomehow() # updates arg1, arg2, and also _cacheSize
i.foo_long(1337, cacheSizeName='_cacheSize') # ref to self._cacheSize