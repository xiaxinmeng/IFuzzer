class S(str):
   def __str__(self): return '__str__ overridden'

class U(unicode):
   def __str__(self): return '__str__ overridden'
   def __unicode__(self): return u'__unicode__ overridden'

s = S()
u = U()