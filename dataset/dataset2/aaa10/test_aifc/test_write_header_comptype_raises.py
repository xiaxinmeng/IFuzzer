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

def test_write_header_comptype_raises():
    for comptype in (b'ULAW', b'ulaw', b'ALAW', b'alaw', b'G722'):
        fout = aifc.open(io.BytesIO(), 'wb')
        fout.setsampwidth(1)
        fout.setcomptype(comptype, b'')
        AIFCLowLevelTest.assertRaises(aifc.Error, fout.close)
        fout.initfp(None)

AIFCLowLevelTest = test_aifc.AIFCLowLevelTest()
test_write_header_comptype_raises()
