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

def test_b16decode():
    eq = BaseXYTestCase.assertEqual
    eq(base64.b16decode(b'0102ABCDEF'), b'\x01\x02\xab\xcd\xef')
    eq(base64.b16decode('0102ABCDEF'), b'\x01\x02\xab\xcd\xef')
    eq(base64.b16decode(b'00'), b'\x00')
    eq(base64.b16decode('00'), b'\x00')
    BaseXYTestCase.assertRaises(binascii.Error, base64.b16decode, b'0102abcdef')
    BaseXYTestCase.assertRaises(binascii.Error, base64.b16decode, '0102abcdef')
    eq(base64.b16decode(b'0102abcdef', True), b'\x01\x02\xab\xcd\xef')
    eq(base64.b16decode('0102abcdef', True), b'\x01\x02\xab\xcd\xef')
    BaseXYTestCase.check_other_types(base64.b16decode, b'0102ABCDEF', b'\x01\x02\xab\xcd\xef')
    BaseXYTestCase.check_decode_type_errors(base64.b16decode)
    eq(base64.b16decode(bytearray(b'0102abcdef'), True), b'\x01\x02\xab\xcd\xef')
    eq(base64.b16decode(memoryview(b'0102abcdef'), True), b'\x01\x02\xab\xcd\xef')
    eq(base64.b16decode(array('B', b'0102abcdef'), True), b'\x01\x02\xab\xcd\xef')
    BaseXYTestCase.assertRaises(binascii.Error, base64.b16decode, '0102AG')
    BaseXYTestCase.assertRaises(binascii.Error, base64.b16decode, '010')

BaseXYTestCase = test_base64.BaseXYTestCase()
test_b16decode()
