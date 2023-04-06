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

def test_namespace_prefixes():
    SetAttributeTest.assertIs(SetAttributeTest.parser.namespace_prefixes, False)
    for x in (0, 1, 2, 0):
        SetAttributeTest.parser.namespace_prefixes = x
        SetAttributeTest.assertIs(SetAttributeTest.parser.namespace_prefixes, bool(x))

SetAttributeTest = test_pyexpat.SetAttributeTest()
SetAttributeTest.setUp()
test_namespace_prefixes()
