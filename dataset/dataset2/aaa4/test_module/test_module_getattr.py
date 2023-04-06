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

def test_module_getattr():
    import test.good_getattr as gga
    from test.good_getattr import test
    ModuleTests.assertEqual(test, 'There is test')
    ModuleTests.assertEqual(gga.x, 1)
    ModuleTests.assertEqual(gga.y, 2)
    with ModuleTests.assertRaisesRegex(AttributeError, 'Deprecated, use whatever instead'):
        gga.yolo
    ModuleTests.assertEqual(gga.whatever, 'There is whatever')
    del sys.modules['test.good_getattr']

ModuleTests = test_module.ModuleTests()
test_module_getattr()
