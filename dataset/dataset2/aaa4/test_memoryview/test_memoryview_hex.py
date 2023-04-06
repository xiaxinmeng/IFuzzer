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

def test_memoryview_hex():
    x = b'0' * 200000
    m1 = memoryview(x)
    m2 = m1[::-1]
    OtherTest.assertEqual(m2.hex(), '30' * 200000)

OtherTest = test_memoryview.OtherTest()
test_memoryview_hex()
