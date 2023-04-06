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

def test_parse_again():
    parser = expat.ParserCreate()
    file = BytesIO(test_pyexpat.data)
    parser.ParseFile(file)
    with ParseTest.assertRaises(expat.error) as cm:
        parser.ParseFile(file)
    ParseTest.assertEqual(expat.ErrorString(cm.exception.code), expat.errors.XML_ERROR_FINISHED)

ParseTest = test_pyexpat.ParseTest()
test_parse_again()
