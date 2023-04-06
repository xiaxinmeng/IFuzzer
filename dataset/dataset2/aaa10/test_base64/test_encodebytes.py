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

def test_encodebytes():
    eq = LegacyBase64TestCase.assertEqual
    eq(base64.encodebytes(b'www.python.org'), b'd3d3LnB5dGhvbi5vcmc=\n')
    eq(base64.encodebytes(b'a'), b'YQ==\n')
    eq(base64.encodebytes(b'ab'), b'YWI=\n')
    eq(base64.encodebytes(b'abc'), b'YWJj\n')
    eq(base64.encodebytes(b''), b'')
    eq(base64.encodebytes(b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#0^&*();:<>,. []{}'), b'YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXpBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWjAxMjM0\nNTY3ODkhQCMwXiYqKCk7Ojw+LC4gW117fQ==\n')
    eq(base64.encodebytes(bytearray(b'abc')), b'YWJj\n')
    eq(base64.encodebytes(memoryview(b'abc')), b'YWJj\n')
    eq(base64.encodebytes(array('B', b'abc')), b'YWJj\n')
    LegacyBase64TestCase.check_type_errors(base64.encodebytes)

LegacyBase64TestCase = test_base64.LegacyBase64TestCase()
test_encodebytes()
