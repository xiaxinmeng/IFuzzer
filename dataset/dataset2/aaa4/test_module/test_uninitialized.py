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

def test_uninitialized():
    foo = test_module.ModuleType.__new__(test_module.ModuleType)
    ModuleTests.assertTrue(foo.__dict__ is None)
    ModuleTests.assertRaises(SystemError, dir, foo)
    try:
        s = foo.__name__
        ModuleTests.fail('__name__ = %s' % repr(s))
    except AttributeError:
        pass
    ModuleTests.assertEqual(foo.__doc__, test_module.ModuleType.__doc__)

ModuleTests = test_module.ModuleTests()
test_uninitialized()
