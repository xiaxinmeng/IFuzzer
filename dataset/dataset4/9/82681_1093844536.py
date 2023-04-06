def method():
   a = 10

mod = reload(old_mod)
old_mod.method.__code__ = mod.method.__code__