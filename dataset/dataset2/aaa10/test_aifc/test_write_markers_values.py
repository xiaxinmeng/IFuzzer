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

def test_write_markers_values():
    fout = aifc.open(io.BytesIO(), 'wb')
    AifcMiscTest.assertEqual(fout.getmarkers(), None)
    fout.setmark(1, 0, b'foo1')
    fout.setmark(1, 1, b'foo2')
    AifcMiscTest.assertEqual(fout.getmark(1), (1, 1, b'foo2'))
    AifcMiscTest.assertEqual(fout.getmarkers(), [(1, 1, b'foo2')])
    fout.initfp(None)

AifcMiscTest = test_aifc.AifcMiscTest()
test_write_markers_values()
