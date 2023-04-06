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

def test_encode_from_stdin():
    with script_helper.spawn_python('-m', 'base64', '-e') as proc:
        (out, err) = proc.communicate(b'a\xffb\n')
    TestMain.assertEqual(out.rstrip(), b'Yf9iCg==')
    TestMain.assertIsNone(err)

TestMain = test_base64.TestMain()
test_encode_from_stdin()
