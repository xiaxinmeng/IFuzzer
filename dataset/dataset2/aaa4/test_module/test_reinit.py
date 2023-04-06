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

def test_reinit():
    foo = test_module.ModuleType('foo', 'foodocሴ')
    foo.bar = 42
    d = foo.__dict__
    foo.__init__('foo', 'foodoc')
    ModuleTests.assertEqual(foo.__name__, 'foo')
    ModuleTests.assertEqual(foo.__doc__, 'foodoc')
    ModuleTests.assertEqual(foo.bar, 42)
    ModuleTests.assertEqual(foo.__dict__, {'__name__': 'foo', '__doc__': 'foodoc', 'bar': 42, '__loader__': None, '__package__': None, '__spec__': None})
    ModuleTests.assertTrue(foo.__dict__ is d)

ModuleTests = test_module.ModuleTests()
test_reinit()
