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

@unittest.skip('XXX test should be adapted for non-byte buffers')
def test_getbuffer():
    pass

AbstractMemoryTests = test_memoryview.AbstractMemoryTests()
test_getbuffer()
