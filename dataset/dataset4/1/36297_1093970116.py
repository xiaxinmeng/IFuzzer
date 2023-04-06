from Zope.ContextWrapper import Wrapper

wl = Wrapper([])
assert isinstance(wl, list) == 1
assert isinstance(wl, Wrapper) == 1