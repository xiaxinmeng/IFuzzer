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

def test_pickle():
    m = memoryview(b'abc')
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        with OtherTest.assertRaises(TypeError):
            pickle.dumps(m, proto)

OtherTest = test_memoryview.OtherTest()
test_pickle()
