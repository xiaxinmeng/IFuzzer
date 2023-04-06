import unittest
from test.support import os_helper
import os
import stat
import sys
import uu
import io
import codecs
import test_uu

def test_decodetwice():
    with open(UUFileTest.tmpin, 'wb') as f:
        f.write(test_uu.encodedtextwrapped(420, UUFileTest.tmpout))
    with open(UUFileTest.tmpin, 'rb') as f:
        uu.decode(f)
    with open(UUFileTest.tmpin, 'rb') as f:
        UUFileTest.assertRaises(uu.Error, uu.decode, f)

UUFileTest = test_uu.UUFileTest()
UUFileTest.setUp()
test_decodetwice()
