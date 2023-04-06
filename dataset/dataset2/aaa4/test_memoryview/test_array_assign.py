import unittest
import test.support
import sys
import gc
import weakref
import array
import io
import copy
import pickle
from test.support import import_helper
import test_memoryview

def test_array_assign():
    a = array.array('i', range(10))
    m = memoryview(a)
    new_a = array.array('i', range(9, -1, -1))
    m[:] = new_a
    ArrayMemoryviewTest.assertEqual(a, new_a)

ArrayMemoryviewTest = test_memoryview.ArrayMemoryviewTest()
test_array_assign()
