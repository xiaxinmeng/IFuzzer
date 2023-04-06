def ishashable(ob):
     try:
         hash(ob)
         return True
     except TypeError:
         return False