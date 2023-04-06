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

def test_tell():
    buf = MemoryTestMixin.buftype('1234567890')
    memio = MemoryTestMixin.ioclass(buf)
    MemoryTestMixin.assertEqual(memio.tell(), 0)
    memio.seek(5)
    MemoryTestMixin.assertEqual(memio.tell(), 5)
    memio.seek(10000)
    MemoryTestMixin.assertEqual(memio.tell(), 10000)
    memio.close()
    MemoryTestMixin.assertRaises(ValueError, memio.tell)

MemoryTestMixin = test_memoryio.MemoryTestMixin()
test_tell()
