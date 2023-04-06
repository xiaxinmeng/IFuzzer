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

def test_read_wrong_compression_type():
    b = b'FORM' + struct.pack('>L', 4) + b'AIFC'
    b += b'COMM' + struct.pack('>LhlhhLL', 23, 1, 0, 8, 16384 | 12, 11025 << 18, 0)
    b += b'WRNG' + struct.pack('B', 0)
    AIFCLowLevelTest.assertRaises(aifc.Error, aifc.open, io.BytesIO(b))

AIFCLowLevelTest = test_aifc.AIFCLowLevelTest()
test_read_wrong_compression_type()
