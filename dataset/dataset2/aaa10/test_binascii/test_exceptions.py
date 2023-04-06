import unittest
import binascii
import array
import re
from test.support import warnings_helper
import test_binascii

def test_exceptions():
    BinASCIITest.assertTrue(issubclass(binascii.Error, Exception))
    BinASCIITest.assertTrue(issubclass(binascii.Incomplete, Exception))

BinASCIITest = test_binascii.BinASCIITest()
test_exceptions()
