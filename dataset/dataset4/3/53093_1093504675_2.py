class Crasher(list): pass
a = () + Crasher() # or Crasher([1])
print(a, type(a), len(a))
#[] <class 'list'> 0 # or [1] <class 'list'> 1