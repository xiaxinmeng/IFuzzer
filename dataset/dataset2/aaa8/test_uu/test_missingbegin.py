import unittest
from test.support import os_helper
import os
import stat
import sys
import uu
import io
import codecs
import test_uu

def test_missingbegin():
    inp = io.BytesIO(b'')
    out = io.BytesIO()
    try:
        uu.decode(inp, out)
        UUTest.fail('No exception raised')
    except uu.Error as e:
        UUTest.assertEqual(str(e), 'No valid begin line found in input file')

UUTest = test_uu.UUTest()
test_missingbegin()
