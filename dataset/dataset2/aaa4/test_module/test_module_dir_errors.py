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

def test_module_dir_errors():
    import test.bad_getattr as bga
    from test import bad_getattr2
    with ModuleTests.assertRaises(TypeError):
        dir(bga)
    with ModuleTests.assertRaises(TypeError):
        dir(bad_getattr2)
    del sys.modules['test.bad_getattr']
    if 'test.bad_getattr2' in sys.modules:
        del sys.modules['test.bad_getattr2']

ModuleTests = test_module.ModuleTests()
test_module_dir_errors()
