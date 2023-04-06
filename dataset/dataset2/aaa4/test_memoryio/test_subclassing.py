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

def test_subclassing():
    buf = MemoryTestMixin.buftype('1234567890')

    def test1():

        class MemIO(MemoryTestMixin.ioclass):
            pass
        m = MemIO(buf)
        return m.getvalue()

    def test2():

        class MemIO(MemoryTestMixin.ioclass):

            def __init__(me, a, b):
                MemoryTestMixin.ioclass.__init__(me, a)
        m = MemIO(buf, None)
        return m.getvalue()
    MemoryTestMixin.assertEqual(test1(), buf)
    MemoryTestMixin.assertEqual(test2(), buf)

MemoryTestMixin = test_memoryio.MemoryTestMixin()
test_subclassing()
