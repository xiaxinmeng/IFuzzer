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

def test_release():
    for tp in AbstractMemoryTests._types:
        b = tp(AbstractMemoryTests._source)
        m = AbstractMemoryTests._view(b)
        m.release()
        AbstractMemoryTests._check_released(m, tp)
        m.release()
        AbstractMemoryTests._check_released(m, tp)

AbstractMemoryTests = test_memoryview.AbstractMemoryTests()
test_release()
