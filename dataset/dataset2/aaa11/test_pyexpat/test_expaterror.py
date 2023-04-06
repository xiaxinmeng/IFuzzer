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

def test_expaterror():
    xml = b'<'
    parser = expat.ParserCreate()
    try:
        parser.Parse(xml, True)
        ErrorMessageTest.fail()
    except expat.ExpatError as e:
        ErrorMessageTest.assertEqual(e.code, errors.codes[errors.XML_ERROR_UNCLOSED_TOKEN])

ErrorMessageTest = test_pyexpat.ErrorMessageTest()
test_expaterror()
