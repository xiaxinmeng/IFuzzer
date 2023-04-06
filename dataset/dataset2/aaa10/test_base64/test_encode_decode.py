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

def test_encode_decode():
    output = TestMain.get_output('-t')
    TestMain.assertSequenceEqual(output.splitlines(), (b"b'Aladdin:open sesame'", b"b'QWxhZGRpbjpvcGVuIHNlc2FtZQ==\\n'", b"b'Aladdin:open sesame'"))

TestMain = test_base64.TestMain()
test_encode_decode()
