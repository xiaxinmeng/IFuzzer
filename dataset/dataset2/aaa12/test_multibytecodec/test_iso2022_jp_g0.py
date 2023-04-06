from test import support
from test.support import os_helper
from test.support.os_helper import TESTFN
import unittest, io, codecs, sys
import _multibytecodec
import test_multibytecodec

def test_iso2022_jp_g0():
    Test_ISO2022.assertNotIn(b'\x0e', '\xad'.encode('iso-2022-jp-2'))
    for encoding in ('iso-2022-jp-2004', 'iso-2022-jp-3'):
        e = '㐆'.encode(encoding)
        Test_ISO2022.assertFalse(any((x > 128 for x in e)))

Test_ISO2022 = test_multibytecodec.Test_ISO2022()
test_iso2022_jp_g0()
