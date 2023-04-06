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

def test_attributes_writable():
    if not AbstractMemoryTests.rw_type:
        AbstractMemoryTests.skipTest('no writable type to test')
    m = AbstractMemoryTests.check_attributes_with_type(AbstractMemoryTests.rw_type)
    AbstractMemoryTests.assertEqual(m.readonly, False)

AbstractMemoryTests = test_memoryview.AbstractMemoryTests()
test_attributes_writable()
