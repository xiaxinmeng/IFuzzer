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

def test_buffering_enabled():
    BufferTextTest.assertTrue(BufferTextTest.parser.buffer_text)
    BufferTextTest.parser.Parse(b'<a>1<b/>2<c/>3</a>', True)
    BufferTextTest.assertEqual(BufferTextTest.stuff, ['123'], 'buffered text not properly collapsed')

BufferTextTest = test_pyexpat.BufferTextTest()
BufferTextTest.setUp()
test_buffering_enabled()
