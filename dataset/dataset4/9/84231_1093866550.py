import unittest
import sys
import _imp

class ModuleSpec:
    pass

class Tests(unittest.TestCase):
    def test_import_fresh(self):
        spec = ModuleSpec()
        spec.sys_weakref = sys.modules["_weakref"]
        spec.name = "_weakref"
        module = _imp.create_builtin(spec)
        module.__spec__ = spec
        sys.modules["_weakref"] = module