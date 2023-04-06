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

def test_decode():
    with open(os_helper.TESTFN, 'wb') as fp:
        fp.write(b'Yf9iCg==')
    output = LegacyBase64TestCase.get_output('-d', os_helper.TESTFN)
    LegacyBase64TestCase.assertEqual(output.rstrip(), b'a\xffb')

LegacyBase64TestCase = test_base64.LegacyBase64TestCase()
test_decode()
