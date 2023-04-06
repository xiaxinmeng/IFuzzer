import unittest
import base64
import binascii
import os
from array import array
from test.support import os_helper
from test.support import script_helper
from io import BytesIO, StringIO
from io import BytesIO, StringIO
import test_base64

def test_encode():
    eq = LegacyBase64TestCase.assertEqual
    from io import BytesIO, StringIO
    infp = BytesIO(b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#0^&*();:<>,. []{}')
    outfp = BytesIO()
    base64.encode(infp, outfp)
    eq(outfp.getvalue(), b'YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXpBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWjAxMjM0\nNTY3ODkhQCMwXiYqKCk7Ojw+LC4gW117fQ==\n')
    LegacyBase64TestCase.assertRaises(TypeError, base64.encode, StringIO('abc'), BytesIO())
    LegacyBase64TestCase.assertRaises(TypeError, base64.encode, BytesIO(b'abc'), StringIO())
    LegacyBase64TestCase.assertRaises(TypeError, base64.encode, StringIO('abc'), StringIO())

LegacyBase64TestCase = test_base64.LegacyBase64TestCase()
test_encode()
