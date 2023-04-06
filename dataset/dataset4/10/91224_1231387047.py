# my_module.py
class First: pass
class Second: pass
class Third: pass

_T = TypeVar('_T', First, Second, Third)
repr(_T)

# ~_T<=(my_module.First, my_module.Second, my_module.Third)