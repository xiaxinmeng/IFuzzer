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

def test_default_to_disabled():
    parser = expat.ParserCreate()
    BufferTextTest.assertFalse(parser.buffer_text)

BufferTextTest = test_pyexpat.BufferTextTest()
test_default_to_disabled()
