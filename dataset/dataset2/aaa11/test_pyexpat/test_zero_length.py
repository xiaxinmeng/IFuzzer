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

def test_zero_length():
    expat.ParserCreate(namespace_separator='')

NamespaceSeparatorTest = test_pyexpat.NamespaceSeparatorTest()
test_zero_length()
