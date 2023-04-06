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

def test_dont_clear_dict():

    def f():
        foo = test_module.ModuleType('foo')
        foo.bar = 4
        return foo
    gc_collect()
    ModuleTests.assertEqual(f().__dict__['bar'], 4)

ModuleTests = test_module.ModuleTests()
test_dont_clear_dict()
