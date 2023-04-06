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

def test_change_size_1():
    xml1 = b"<?xml version='1.0' encoding='iso8859'?><a><s>" + b'a' * 1024
    xml2 = b'aaa</s><s>' + b'a' * 1025 + b'</s></a>'
    parser = expat.ParserCreate()
    parser.CharacterDataHandler = ChardataBufferTest.counting_handler
    parser.buffer_text = 1
    parser.buffer_size = 1024
    ChardataBufferTest.assertEqual(parser.buffer_size, 1024)
    ChardataBufferTest.n = 0
    parser.Parse(xml1, False)
    parser.buffer_size *= 2
    ChardataBufferTest.assertEqual(parser.buffer_size, 2048)
    parser.Parse(xml2, True)
    ChardataBufferTest.assertEqual(ChardataBufferTest.n, 2)

ChardataBufferTest = test_pyexpat.ChardataBufferTest()
test_change_size_1()
