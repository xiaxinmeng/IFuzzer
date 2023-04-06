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

def test_b32decode():
    eq = BaseXYTestCase.assertEqual
    tests = {b'': b'', b'AA======': b'\x00', b'ME======': b'a', b'MFRA====': b'ab', b'MFRGG===': b'abc', b'MFRGGZA=': b'abcd', b'MFRGGZDF': b'abcde'}
    for (data, res) in tests.items():
        eq(base64.b32decode(data), res)
        eq(base64.b32decode(data.decode('ascii')), res)
    BaseXYTestCase.check_other_types(base64.b32decode, b'MFRGG===', b'abc')
    BaseXYTestCase.check_decode_type_errors(base64.b32decode)

BaseXYTestCase = test_base64.BaseXYTestCase()
test_b32decode()
