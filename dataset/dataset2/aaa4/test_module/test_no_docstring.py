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

def test_no_docstring():
    foo = test_module.ModuleType('foo')
    ModuleTests.assertEqual(foo.__name__, 'foo')
    ModuleTests.assertEqual(foo.__doc__, None)
    ModuleTests.assertIs(foo.__loader__, None)
    ModuleTests.assertIs(foo.__package__, None)
    ModuleTests.assertIs(foo.__spec__, None)
    ModuleTests.assertEqual(foo.__dict__, {'__name__': 'foo', '__doc__': None, '__loader__': None, '__package__': None, '__spec__': None})

ModuleTests = test_module.ModuleTests()
test_no_docstring()
