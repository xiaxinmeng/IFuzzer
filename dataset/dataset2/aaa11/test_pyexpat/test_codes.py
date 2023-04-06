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

def test_codes():
    ErrorMessageTest.assertEqual(errors.XML_ERROR_SYNTAX, errors.messages[errors.codes[errors.XML_ERROR_SYNTAX]])

ErrorMessageTest = test_pyexpat.ErrorMessageTest()
test_codes()
