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

def test_bytes_array():
    buf = b'1234567890'
    import array
    a = array.array('b', list(buf))
    memio = PyBytesIOTest.ioclass(a)
    PyBytesIOTest.assertEqual(memio.getvalue(), buf)
    PyBytesIOTest.assertEqual(memio.write(a), 10)
    PyBytesIOTest.assertEqual(memio.getvalue(), buf)

PyBytesIOTest = test_memoryio.PyBytesIOTest()
test_bytes_array()
