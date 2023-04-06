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

def test_toreadonly():
    for tp in AbstractMemoryTests._types:
        b = tp(AbstractMemoryTests._source)
        m = AbstractMemoryTests._view(b)
        mm = m.toreadonly()
        AbstractMemoryTests.assertTrue(mm.readonly)
        AbstractMemoryTests.assertTrue(memoryview(mm).readonly)
        AbstractMemoryTests.assertEqual(mm.tolist(), m.tolist())
        mm.release()
        m.tolist()

AbstractMemoryTests = test_memoryview.AbstractMemoryTests()
test_toreadonly()
