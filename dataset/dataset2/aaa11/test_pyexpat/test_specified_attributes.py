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

def test_specified_attributes():
    SetAttributeTest.assertIs(SetAttributeTest.parser.specified_attributes, False)
    for x in (0, 1, 2, 0):
        SetAttributeTest.parser.specified_attributes = x
        SetAttributeTest.assertIs(SetAttributeTest.parser.specified_attributes, bool(x))

SetAttributeTest = test_pyexpat.SetAttributeTest()
SetAttributeTest.setUp()
test_specified_attributes()
