import unittest
import binascii
import array
import re
from test.support import warnings_helper
import test_binascii

def test_functions():
    for name in test_binascii.all_functions:
        BinASCIITest.assertTrue(hasattr(getattr(binascii, name), '__call__'))
        BinASCIITest.assertRaises(TypeError, getattr(binascii, name))

BinASCIITest = test_binascii.BinASCIITest()
test_functions()
