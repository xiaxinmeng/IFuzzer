import unittest
from test import support
import io
import _pyio as pyio
import pickle
import sys
import __main__
import array
import array
import test_memoryio

def test_flush():
    buf = MemoryTestMixin.buftype('1234567890')
    memio = MemoryTestMixin.ioclass(buf)
    MemoryTestMixin.assertEqual(memio.flush(), None)

MemoryTestMixin = test_memoryio.MemoryTestMixin()
test_flush()
