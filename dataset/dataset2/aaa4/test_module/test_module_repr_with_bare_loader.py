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

def test_module_repr_with_bare_loader():
    m = test_module.ModuleType('foo')
    m.__loader__ = test_module.BareLoader
    module_repr = repr(test_module.BareLoader)
    ModuleTests.assertEqual(repr(m), "<module 'foo' ({})>".format(module_repr))

ModuleTests = test_module.ModuleTests()
test_module_repr_with_bare_loader()
