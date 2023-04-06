import importlib.metadata as metadata
from os.path import dirname

numpy_where = dirname(dirname(__spec__.origin))
dist, = metadata.distributions('numpy', path=[numpy_where])
__version__ = dist.version