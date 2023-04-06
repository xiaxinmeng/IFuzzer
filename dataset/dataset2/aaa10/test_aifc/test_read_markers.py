from test.support import findfile
from test.support.os_helper import TESTFN, unlink
from test.support.warnings_helper import check_no_resource_warning
import unittest
from unittest import mock
from test import audiotests
from audioop import byteswap
import io
import sys
import struct
import aifc
import test_aifc

def test_read_markers():
    fout = AifcMiscTest.fout = aifc.open(TESTFN, 'wb')
    fout.aiff()
    fout.setparams((1, 1, 1, 1, b'NONE', b''))
    fout.setmark(1, 0, b'odd')
    fout.setmark(2, 0, b'even')
    fout.writeframes(b'\x00')
    fout.close()
    f = aifc.open(TESTFN, 'rb')
    AifcMiscTest.addCleanup(f.close)
    AifcMiscTest.assertEqual(f.getmarkers(), [(1, 0, b'odd'), (2, 0, b'even')])
    AifcMiscTest.assertEqual(f.getmark(1), (1, 0, b'odd'))
    AifcMiscTest.assertEqual(f.getmark(2), (2, 0, b'even'))
    AifcMiscTest.assertRaises(aifc.Error, f.getmark, 3)

AifcMiscTest = test_aifc.AifcMiscTest()
test_read_markers()
