import unittest
import binascii
import array
import re
from test.support import warnings_helper
import test_binascii

def test_crc32():
    crc = binascii.crc32(BinASCIITest.type2test(b'Test the CRC-32 of'))
    crc = binascii.crc32(BinASCIITest.type2test(b' this string.'), crc)
    BinASCIITest.assertEqual(crc, 1571220330)
    BinASCIITest.assertRaises(TypeError, binascii.crc32)

BinASCIITest = test_binascii.BinASCIITest()
test_crc32()
