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

def test_b32hexencode():
    test_cases = [(b'', b''), (b'\x00', b'00======'), (b'a', b'C4======'), (b'ab', b'C5H0===='), (b'abc', b'C5H66==='), (b'abcd', b'C5H66P0='), (b'abcde', b'C5H66P35')]
    for (to_encode, expected) in test_cases:
        with BaseXYTestCase.subTest(to_decode=to_encode):
            BaseXYTestCase.assertEqual(base64.b32hexencode(to_encode), expected)

BaseXYTestCase = test_base64.BaseXYTestCase()
test_b32hexencode()
