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

def test_read_comm_kludge_compname_even():
    b = b'FORM' + struct.pack('>L', 4) + b'AIFC'
    b += b'COMM' + struct.pack('>LhlhhLL', 18, 1, 0, 8, 16384 | 12, 11025 << 18, 0)
    b += b'NONE' + struct.pack('B', 4) + b'even' + b'\x00'
    b += b'SSND' + struct.pack('>L', 8) + b'\x00' * 8
    with AIFCLowLevelTest.assertWarns(UserWarning) as cm:
        f = aifc.open(io.BytesIO(b))
    AIFCLowLevelTest.assertEqual(str(cm.warning), 'Warning: bad COMM chunk size')
    AIFCLowLevelTest.assertEqual(f.getcompname(), b'even')

AIFCLowLevelTest = test_aifc.AIFCLowLevelTest()
test_read_comm_kludge_compname_even()
