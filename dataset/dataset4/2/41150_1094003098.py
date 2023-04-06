class Direct:
  def __reduce__(self): return id,(self,) # obviously impossible
class Indirect:
  # Can't create either the new object or the tuple first!
  def __reduce__(self): return id,((self,),)