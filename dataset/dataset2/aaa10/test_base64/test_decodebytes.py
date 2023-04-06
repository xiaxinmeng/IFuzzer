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

def test_decodebytes():
    eq = LegacyBase64TestCase.assertEqual
    eq(base64.decodebytes(b'd3d3LnB5dGhvbi5vcmc=\n'), b'www.python.org')
    eq(base64.decodebytes(b'YQ==\n'), b'a')
    eq(base64.decodebytes(b'YWI=\n'), b'ab')
    eq(base64.decodebytes(b'YWJj\n'), b'abc')
    eq(base64.decodebytes(b'YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXpBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWjAxMjM0\nNTY3ODkhQCMwXiYqKCk7Ojw+LC4gW117fQ==\n'), b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#0^&*();:<>,. []{}')
    eq(base64.decodebytes(b''), b'')
    eq(base64.decodebytes(bytearray(b'YWJj\n')), b'abc')
    eq(base64.decodebytes(memoryview(b'YWJj\n')), b'abc')
    eq(base64.decodebytes(array('B', b'YWJj\n')), b'abc')
    LegacyBase64TestCase.check_type_errors(base64.decodebytes)

LegacyBase64TestCase = test_base64.LegacyBase64TestCase()
test_decodebytes()
