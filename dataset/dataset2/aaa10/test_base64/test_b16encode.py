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

def test_b16encode():
    eq = BaseXYTestCase.assertEqual
    eq(base64.b16encode(b'\x01\x02\xab\xcd\xef'), b'0102ABCDEF')
    eq(base64.b16encode(b'\x00'), b'00')
    BaseXYTestCase.check_other_types(base64.b16encode, b'\x01\x02\xab\xcd\xef', b'0102ABCDEF')
    BaseXYTestCase.check_encode_type_errors(base64.b16encode)

BaseXYTestCase = test_base64.BaseXYTestCase()
test_b16encode()
