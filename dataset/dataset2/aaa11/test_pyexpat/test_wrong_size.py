from io import BytesIO
import os
import platform
import sys
import sysconfig
import unittest
import traceback
from xml.parsers import expat
from xml.parsers.expat import errors
from test.support import sortdict
import test_pyexpat

def test_wrong_size():
    parser = expat.ParserCreate()
    parser.buffer_text = 1
    with ChardataBufferTest.assertRaises(ValueError):
        parser.buffer_size = -1
    with ChardataBufferTest.assertRaises(ValueError):
        parser.buffer_size = 0
    with ChardataBufferTest.assertRaises((ValueError, OverflowError)):
        parser.buffer_size = sys.maxsize + 1
    with ChardataBufferTest.assertRaises(TypeError):
        parser.buffer_size = 512.0

ChardataBufferTest = test_pyexpat.ChardataBufferTest()
test_wrong_size()
