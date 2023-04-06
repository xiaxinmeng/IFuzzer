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

def test_issue5449():
    buf = PyBytesIOTest.buftype('1234567890')
    PyBytesIOTest.ioclass(initial_bytes=buf)
    PyBytesIOTest.assertRaises(TypeError, PyBytesIOTest.ioclass, buf, foo=None)

PyBytesIOTest = test_memoryio.PyBytesIOTest()
test_issue5449()
