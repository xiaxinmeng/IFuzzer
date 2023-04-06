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

def test_a85_padding():
    eq = BaseXYTestCase.assertEqual
    eq(base64.a85encode(b'x', pad=True), b'GQ7^D')
    eq(base64.a85encode(b'xx', pad=True), b"G^'2g")
    eq(base64.a85encode(b'xxx', pad=True), b'G^+H5')
    eq(base64.a85encode(b'xxxx', pad=True), b'G^+IX')
    eq(base64.a85encode(b'xxxxx', pad=True), b'G^+IXGQ7^D')
    eq(base64.a85decode(b'GQ7^D'), b'x\x00\x00\x00')
    eq(base64.a85decode(b"G^'2g"), b'xx\x00\x00')
    eq(base64.a85decode(b'G^+H5'), b'xxx\x00')
    eq(base64.a85decode(b'G^+IX'), b'xxxx')
    eq(base64.a85decode(b'G^+IXGQ7^D'), b'xxxxx\x00\x00\x00')

BaseXYTestCase = test_base64.BaseXYTestCase()
test_a85_padding()
