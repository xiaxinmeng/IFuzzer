while doafterhandler:
    doafterhandler.pop(0)()
# is O(n*2)

doafterhandler.reverse()
while doafterhandler:
  doafterhandler.pop()()
# is O(n)

for f in doafterhandler:
    f()
doafterhandler[:] = []
# doafterhandler.clear() works in 3.3
# is also O(n) and replaces repeated .pop with one clear