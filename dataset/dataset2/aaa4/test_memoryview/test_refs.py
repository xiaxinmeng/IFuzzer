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

def test_refs():
    for tp in BaseMemorySliceTests._types:
        m = memoryview(tp(BaseMemorySliceTests._source))
        oldrefcount = sys.getrefcount(m)
        m[1:2]
        BaseMemorySliceTests.assertEqual(sys.getrefcount(m), oldrefcount)

BaseMemorySliceTests = test_memoryview.BaseMemorySliceTests()
test_refs()
