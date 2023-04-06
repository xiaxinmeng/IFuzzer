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

def test_getbuf_fail():
    AbstractMemoryTests.assertRaises(TypeError, AbstractMemoryTests._view, {})

AbstractMemoryTests = test_memoryview.AbstractMemoryTests()
test_getbuf_fail()
