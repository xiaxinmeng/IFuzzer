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

def test_invalid_attributes():
    with SetAttributeTest.assertRaises(AttributeError):
        SetAttributeTest.parser.returns_unicode = 1
    with SetAttributeTest.assertRaises(AttributeError):
        SetAttributeTest.parser.returns_unicode
    SetAttributeTest.assertRaises(TypeError, setattr, SetAttributeTest.parser, range(15), 0)
    SetAttributeTest.assertRaises(TypeError, SetAttributeTest.parser.__setattr__, range(15), 0)
    SetAttributeTest.assertRaises(TypeError, getattr, SetAttributeTest.parser, range(15))

SetAttributeTest = test_pyexpat.SetAttributeTest()
SetAttributeTest.setUp()
test_invalid_attributes()
