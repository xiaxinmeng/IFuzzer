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

def test_read_wrong_marks():
    b = b'FORM' + struct.pack('>L', 4) + b'AIFF'
    b += b'COMM' + struct.pack('>LhlhhLL', 18, 1, 0, 8, 16384 | 12, 11025 << 18, 0)
    b += b'SSND' + struct.pack('>L', 8) + b'\x00' * 8
    b += b'MARK' + struct.pack('>LhB', 3, 1, 1)
    with AIFCLowLevelTest.assertWarns(UserWarning) as cm:
        f = aifc.open(io.BytesIO(b))
    AIFCLowLevelTest.assertEqual(str(cm.warning), 'Warning: MARK chunk contains only 0 markers instead of 1')
    AIFCLowLevelTest.assertEqual(f.getmarkers(), None)

AIFCLowLevelTest = test_aifc.AIFCLowLevelTest()
test_read_wrong_marks()
