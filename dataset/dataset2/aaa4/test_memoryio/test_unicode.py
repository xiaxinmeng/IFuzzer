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

def test_unicode():
    memio = PyBytesIOTest.ioclass()
    PyBytesIOTest.assertRaises(TypeError, PyBytesIOTest.ioclass, '1234567890')
    PyBytesIOTest.assertRaises(TypeError, memio.write, '1234567890')
    PyBytesIOTest.assertRaises(TypeError, memio.writelines, ['1234567890'])

PyBytesIOTest = test_memoryio.PyBytesIOTest()
test_unicode()
