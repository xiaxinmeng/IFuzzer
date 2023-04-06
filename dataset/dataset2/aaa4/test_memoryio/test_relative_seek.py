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

def test_relative_seek():
    memio = PyBytesIOTest.ioclass()
    PyBytesIOTest.assertRaises(OSError, memio.seek, -1, 1)
    PyBytesIOTest.assertRaises(OSError, memio.seek, 3, 1)
    PyBytesIOTest.assertRaises(OSError, memio.seek, -3, 1)
    PyBytesIOTest.assertRaises(OSError, memio.seek, -1, 2)
    PyBytesIOTest.assertRaises(OSError, memio.seek, 1, 1)
    PyBytesIOTest.assertRaises(OSError, memio.seek, 1, 2)

PyBytesIOTest = test_memoryio.PyBytesIOTest()
test_relative_seek()
