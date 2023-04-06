def deco(x = None):
    def inner(fn):
         if not x:
             x = somedefaultvalue
    
    return inner