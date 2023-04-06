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

def test_overseek():
    buf = MemoryTestMixin.buftype('1234567890')
    memio = MemoryTestMixin.ioclass(buf)
    MemoryTestMixin.assertEqual(memio.seek(len(buf) + 1), 11)
    MemoryTestMixin.assertEqual(memio.read(), MemoryTestMixin.EOF)
    MemoryTestMixin.assertEqual(memio.tell(), 11)
    MemoryTestMixin.assertEqual(memio.getvalue(), buf)
    memio.write(MemoryTestMixin.EOF)
    MemoryTestMixin.assertEqual(memio.getvalue(), buf)
    memio.write(buf)
    MemoryTestMixin.assertEqual(memio.getvalue(), buf + MemoryTestMixin.buftype('\x00') + buf)

MemoryTestMixin = test_memoryio.MemoryTestMixin()
test_overseek()
