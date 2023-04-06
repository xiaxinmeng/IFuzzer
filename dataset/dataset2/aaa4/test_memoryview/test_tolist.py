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

@unittest.skip('XXX NotImplementedError: tolist() only supports byte views')
def test_tolist():
    pass

AbstractMemoryTests = test_memoryview.AbstractMemoryTests()
test_tolist()
