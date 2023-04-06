import unittest
import weakref
from test.support import gc_collect
from test.support.script_helper import assert_python_ok
import sys
import test.good_getattr as gga
from test.good_getattr import test
import test.bad_getattr as bga
from test import bad_getattr2
import test.good_getattr as gga
import test.bad_getattr as bga
from test import bad_getattr2
from test import bad_getattr3
import test_module

def test_module_getattr_errors():
    import test.bad_getattr as bga
    from test import bad_getattr2
    ModuleTests.assertEqual(bga.x, 1)
    ModuleTests.assertEqual(bad_getattr2.x, 1)
    with ModuleTests.assertRaises(TypeError):
        bga.nope
    with ModuleTests.assertRaises(TypeError):
        bad_getattr2.nope
    del sys.modules['test.bad_getattr']
    if 'test.bad_getattr2' in sys.modules:
        del sys.modules['test.bad_getattr2']

ModuleTests = test_module.ModuleTests()
test_module_getattr_errors()
