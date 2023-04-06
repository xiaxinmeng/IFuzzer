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

def test_decode_nonascii_str():
    decode_funcs = (base64.b64decode, base64.standard_b64decode, base64.urlsafe_b64decode, base64.b32decode, base64.b16decode, base64.b85decode, base64.a85decode)
    for f in decode_funcs:
        BaseXYTestCase.assertRaises(ValueError, f, 'with non-ascii Ë')

BaseXYTestCase = test_base64.BaseXYTestCase()
test_decode_nonascii_str()
