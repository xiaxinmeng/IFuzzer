from errno import ENODATA
from os import getxattr, setxattr
from pathlib import Path

class Path_(type(Path())):

    __slots__ = ("new_attr",)

    def __new__(cls, *args, new_attr=None, **kwargs):
        self = super().__new__(cls, *args, **kwargs)
        self._new_attr = new_attr
        return self

    @property
    def new_attr(self):
        if self._new_attr:
            return self._new_attr