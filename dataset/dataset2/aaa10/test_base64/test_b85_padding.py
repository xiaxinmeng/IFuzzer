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

def test_b85_padding():
    eq = BaseXYTestCase.assertEqual
    eq(base64.b85encode(b'x', pad=True), b'cmMzZ')
    eq(base64.b85encode(b'xx', pad=True), b'cz6H+')
    eq(base64.b85encode(b'xxx', pad=True), b'czAdK')
    eq(base64.b85encode(b'xxxx', pad=True), b'czAet')
    eq(base64.b85encode(b'xxxxx', pad=True), b'czAetcmMzZ')
    eq(base64.b85decode(b'cmMzZ'), b'x\x00\x00\x00')
    eq(base64.b85decode(b'cz6H+'), b'xx\x00\x00')
    eq(base64.b85decode(b'czAdK'), b'xxx\x00')
    eq(base64.b85decode(b'czAet'), b'xxxx')
    eq(base64.b85decode(b'czAetcmMzZ'), b'xxxxx\x00\x00\x00')

BaseXYTestCase = test_base64.BaseXYTestCase()
test_b85_padding()
