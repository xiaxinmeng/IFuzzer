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

def test_descriptor_errors_propagate():

    class Descr:

        def __get__(ModuleTests, o, t):
            raise RuntimeError

    class M(test_module.ModuleType):
        melon = Descr()
    ModuleTests.assertRaises(RuntimeError, getattr, M('mymod'), 'melon')

ModuleTests = test_module.ModuleTests()
test_descriptor_errors_propagate()
