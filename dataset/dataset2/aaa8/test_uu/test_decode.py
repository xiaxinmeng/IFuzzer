import unittest
from test.support import os_helper
import os
import stat
import sys
import uu
import io
import codecs
import test_uu

def test_decode():
    with open(UUTest.tmpin, 'wb') as f:
        f.write(encodedtextwrapped(420, UUTest.tmpout))
    with open(UUTest.tmpin, 'rb') as f:
        uu.decode(f)
    with open(UUTest.tmpout, 'rb') as f:
        s = f.read()
    UUTest.assertEqual(s, plaintext)

UUTest = test_uu.UUTest()
UUTest.setUp()
test_decode()
