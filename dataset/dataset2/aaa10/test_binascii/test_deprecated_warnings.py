import unittest
import binascii
import array
import re
from test.support import warnings_helper
import test_binascii

def test_deprecated_warnings():
    with BinASCIITest.assertWarns(DeprecationWarning):
        BinASCIITest.assertEqual(binascii.b2a_hqx(b'abc'), b'B@*M')
    with BinASCIITest.assertWarns(DeprecationWarning):
        BinASCIITest.assertEqual(binascii.a2b_hqx(b'B@*M'), (b'abc', 0))
    with BinASCIITest.assertWarns(DeprecationWarning):
        BinASCIITest.assertEqual(binascii.rlecode_hqx(b'a' * 10), b'a\x90\n')
    with BinASCIITest.assertWarns(DeprecationWarning):
        BinASCIITest.assertEqual(binascii.rledecode_hqx(b'a\x90\n'), b'a' * 10)

BinASCIITest = test_binascii.BinASCIITest()
test_deprecated_warnings()
