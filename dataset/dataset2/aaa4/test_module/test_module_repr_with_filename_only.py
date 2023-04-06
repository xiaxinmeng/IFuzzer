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

def test_module_repr_with_filename_only():
    m = test_module.ModuleType('foo')
    del m.__name__
    m.__file__ = '/tmp/foo.py'
    ModuleTests.assertEqual(repr(m), "<module '?' from '/tmp/foo.py'>")

ModuleTests = test_module.ModuleTests()
test_module_repr_with_filename_only()
