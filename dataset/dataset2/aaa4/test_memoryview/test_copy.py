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

def test_copy():
    m = memoryview(b'abc')
    with OtherTest.assertRaises(TypeError):
        copy.copy(m)

OtherTest = test_memoryview.OtherTest()
test_copy()
