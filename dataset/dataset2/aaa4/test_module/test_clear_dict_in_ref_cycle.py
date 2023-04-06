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

def test_clear_dict_in_ref_cycle():
    destroyed = []
    m = test_module.ModuleType('foo')
    m.destroyed = destroyed
    s = 'class A:\n    def __init__(ModuleTests, l):\n        ModuleTests.l = l\n    def __del__(ModuleTests):\n        ModuleTests.l.append(1)\na = A(destroyed)'
    exec(s, m.__dict__)
    del m
    gc_collect()
    ModuleTests.assertEqual(destroyed, [1])

ModuleTests = test_module.ModuleTests()
test_clear_dict_in_ref_cycle()
