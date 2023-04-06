## leak.py
## >>> import imp, leak; imp.reload(leak)
## will leak ~2.5mb per reload
## on i386 debian unstable machine (according to top).
## in my real world app (an automatic build system),
## i run out of memory after a number reloads :(
class Foo(object): pass
Foo.leaky_dictionary = {}
for aa in range(256):
  for bb in range(256):
    Foo.leaky_dictionary[(bb << 8) | aa] = None