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

def test_getitem():
    for tp in AbstractMemoryTests._types:
        AbstractMemoryTests.check_getitem_with_type(tp)

AbstractMemoryTests = test_memoryview.AbstractMemoryTests()
test_getitem()
