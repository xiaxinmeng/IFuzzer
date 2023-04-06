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

def test_illegal():
    try:
        expat.ParserCreate(namespace_separator=42)
        NamespaceSeparatorTest.fail()
    except TypeError as e:
        NamespaceSeparatorTest.assertEqual(str(e), "ParserCreate() argument 'namespace_separator' must be str or None, not int")
    try:
        expat.ParserCreate(namespace_separator='too long')
        NamespaceSeparatorTest.fail()
    except ValueError as e:
        NamespaceSeparatorTest.assertEqual(str(e), 'namespace_separator must be at most one character, omitted, or None')

NamespaceSeparatorTest = test_pyexpat.NamespaceSeparatorTest()
test_illegal()
