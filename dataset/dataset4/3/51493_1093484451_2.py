# zip_longest as it is in the documentation:
def zip_longest(*args, fillvalue=None):
   # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
   def sentinel(counter = ([fillvalue]*(len(args)-1)).pop):
       yield counter()         # yields the fillvalue, or raises IndexError
   fillers = repeat(fillvalue)
   iters = [chain(it, sentinel(), fillers) for it in args]
   try:
       for tup in zip(*iters):
           yield tup
   except IndexError:
       pass