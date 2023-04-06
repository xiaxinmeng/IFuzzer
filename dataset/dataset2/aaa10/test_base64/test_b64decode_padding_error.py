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

def test_b64decode_padding_error():
    BaseXYTestCase.assertRaises(binascii.Error, base64.b64decode, b'abc')
    BaseXYTestCase.assertRaises(binascii.Error, base64.b64decode, 'abc')

BaseXYTestCase = test_base64.BaseXYTestCase()
test_b64decode_padding_error()
