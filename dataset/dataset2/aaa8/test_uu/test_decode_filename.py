import unittest
from test.support import os_helper
import os
import stat
import sys
import uu
import io
import codecs
import test_uu

def test_decode_filename():
    with open(UUFileTest.tmpin, 'wb') as f:
        f.write(test_uu.encodedtextwrapped(420, UUFileTest.tmpout))
    uu.decode(UUFileTest.tmpin)
    with open(UUFileTest.tmpout, 'rb') as f:
        s = f.read()
    UUFileTest.assertEqual(s, test_uu.plaintext)

UUFileTest = test_uu.UUFileTest()
UUFileTest.setUp()
test_decode_filename()
