
from importlib import resources

r = resources.files(__name__) / 'res.txt'

print(repr(type(r.name)))
