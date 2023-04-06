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

def test_encode_file():
    with open(os_helper.TESTFN, 'wb') as fp:
        fp.write(b'a\xffb\n')
    output = TestMain.get_output('-e', os_helper.TESTFN)
    TestMain.assertEqual(output.rstrip(), b'Yf9iCg==')

TestMain = test_base64.TestMain()
test_encode_file()
