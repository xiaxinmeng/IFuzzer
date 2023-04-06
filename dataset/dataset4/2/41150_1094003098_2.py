class Switch:
  def __reduce__(self): return id,(self.lst,)
a=Switch(); b=Switch()
a.list=[b,a]; b.list=[a,b]