from Zope.ContextWrapper import Wrapper

wl = Wrapper([])
assert isinstance(wl, list) is 1
assert isinstance(wl, Wrapper) is 1