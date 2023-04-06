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

def test_unchanged_size():
    xml1 = b"<?xml version='1.0' encoding='iso8859'?><s>" + b'a' * 512
    xml2 = b'a' * 512 + b'</s>'
    parser = expat.ParserCreate()
    parser.CharacterDataHandler = ChardataBufferTest.counting_handler
    parser.buffer_size = 512
    parser.buffer_text = 1
    ChardataBufferTest.n = 0
    parser.Parse(xml1)
    ChardataBufferTest.assertEqual(ChardataBufferTest.n, 1)
    parser.buffer_size = parser.buffer_size
    ChardataBufferTest.assertEqual(ChardataBufferTest.n, 1)
    parser.Parse(xml2)
    ChardataBufferTest.assertEqual(ChardataBufferTest.n, 2)

ChardataBufferTest = test_pyexpat.ChardataBufferTest()
test_unchanged_size()
