import unittest
from test.support import os_helper
import os
import stat
import sys
import uu
import io
import codecs
import test_uu

def test_truncatedinput():
    inp = io.BytesIO(b'begin 644 t1\n' + test_uu.encodedtext)
    out = io.BytesIO()
    try:
        uu.decode(inp, out)
        UUTest.fail('No exception raised')
    except uu.Error as e:
        UUTest.assertEqual(str(e), 'Truncated input file')

UUTest = test_uu.UUTest()
test_truncatedinput()
