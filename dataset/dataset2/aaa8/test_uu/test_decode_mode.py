import unittest
from test.support import os_helper
import os
import stat
import sys
import uu
import io
import codecs
import test_uu

def test_decode_mode():
    expected_mode = 292
    with open(UUFileTest.tmpin, 'wb') as f:
        f.write(test_uu.encodedtextwrapped(expected_mode, UUFileTest.tmpout))
    UUFileTest.addCleanup(os.chmod, UUFileTest.tmpout, expected_mode | stat.S_IWRITE)
    with open(UUFileTest.tmpin, 'rb') as f:
        uu.decode(f)
    UUFileTest.assertEqual(stat.S_IMODE(os.stat(UUFileTest.tmpout).st_mode), expected_mode)

UUFileTest = test_uu.UUFileTest()
UUFileTest.setUp()
test_decode_mode()
