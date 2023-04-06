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

def test_weakref():
    m = test_module.ModuleType('foo')
    wr = weakref.ref(m)
    ModuleTests.assertIs(wr(), m)
    del m
    gc_collect()
    ModuleTests.assertIs(wr(), None)

ModuleTests = test_module.ModuleTests()
test_weakref()
