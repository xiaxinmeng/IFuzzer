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

def test_read1():
    buf = PyBytesIOTest.buftype('1234567890')
    PyBytesIOTest.assertEqual(PyBytesIOTest.ioclass(buf).read1(), buf)
    PyBytesIOTest.assertEqual(PyBytesIOTest.ioclass(buf).read1(-1), buf)

PyBytesIOTest = test_memoryio.PyBytesIOTest()
test_read1()
