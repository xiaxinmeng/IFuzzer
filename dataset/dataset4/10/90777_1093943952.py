
"""
>>> print(static_property)
static value
>>> print(lazy_property)
lazy value
"""
# text.py
import types
import sys


static_property = 'static value'


class _Properties(types.ModuleType):
    @property
    def lazy_property(self):
        return 'lazy value'


sys.modules[__name__].__class__ = _Properties
