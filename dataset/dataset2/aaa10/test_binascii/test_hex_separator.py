import unittest
import binascii
import array
import re
from test.support import warnings_helper
import test_binascii

def test_hex_separator():
    """Test that hexlify and b2a_hex are binary versions of bytes.hex."""
    s = b'{s\x05\x00\x00\x00worldi\x02\x00\x00\x00s\x05\x00\x00\x00helloi\x01\x00\x00\x000'
    BinASCIITest.assertEqual(binascii.hexlify(BinASCIITest.type2test(s)), s.hex().encode('ascii'))
    expected8 = s.hex('.', 8).encode('ascii')
    BinASCIITest.assertEqual(binascii.hexlify(BinASCIITest.type2test(s), '.', 8), expected8)
    expected1 = s.hex(':').encode('ascii')
    BinASCIITest.assertEqual(binascii.b2a_hex(BinASCIITest.type2test(s), ':'), expected1)

BinASCIITest = test_binascii.BinASCIITest()
test_hex_separator()
