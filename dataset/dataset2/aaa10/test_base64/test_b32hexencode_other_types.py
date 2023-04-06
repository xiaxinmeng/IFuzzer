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

def test_b32hexencode_other_types():
    BaseXYTestCase.check_other_types(base64.b32hexencode, b'abcd', b'C5H66P0=')
    BaseXYTestCase.check_encode_type_errors(base64.b32hexencode)

BaseXYTestCase = test_base64.BaseXYTestCase()
test_b32hexencode_other_types()
