from __future__ import lazy_imports

try:
    from _c_accelerator import foo
except ImportError:
    def foo(): ...