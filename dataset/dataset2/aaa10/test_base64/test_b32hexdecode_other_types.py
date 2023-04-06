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

def test_b32hexdecode_other_types():
    BaseXYTestCase.check_other_types(base64.b32hexdecode, b'C5H66===', b'abc')
    BaseXYTestCase.check_decode_type_errors(base64.b32hexdecode)

BaseXYTestCase = test_base64.BaseXYTestCase()
test_b32hexdecode_other_types()
