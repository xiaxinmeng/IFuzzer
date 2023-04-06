help("compile") # this works
import __builtin__
real_import = __import__
__builtin__.__import__ = lambda *a: real_import(*a)
help("compile") # this fails