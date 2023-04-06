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

def test_b32encode():
    eq = BaseXYTestCase.assertEqual
    eq(base64.b32encode(b''), b'')
    eq(base64.b32encode(b'\x00'), b'AA======')
    eq(base64.b32encode(b'a'), b'ME======')
    eq(base64.b32encode(b'ab'), b'MFRA====')
    eq(base64.b32encode(b'abc'), b'MFRGG===')
    eq(base64.b32encode(b'abcd'), b'MFRGGZA=')
    eq(base64.b32encode(b'abcde'), b'MFRGGZDF')
    BaseXYTestCase.check_other_types(base64.b32encode, b'abcd', b'MFRGGZA=')
    BaseXYTestCase.check_encode_type_errors(base64.b32encode)

BaseXYTestCase = test_base64.BaseXYTestCase()
test_b32encode()
