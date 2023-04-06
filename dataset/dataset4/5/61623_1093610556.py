class Meta(type):
    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        return ClassMapping()

from collections import MutableMapping
class ClassMapping(MutableMapping):
    def __init__(self, *args, **kwargs):
        self._dict = dict(*args, **kwargs)
    def __len__(self):
      return len(self._dict)
    def __iter__(self):
        return iter(self._dict)
    def __getitem__(self, key):
        return self._dict[key]
    def __setitem__(self, key, value):
        self._dict[key] = value
    def __delitem__(self, key):
        del self._dict[key]