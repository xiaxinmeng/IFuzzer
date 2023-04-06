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

def test_read_wrong_sample_width():
    for sampwidth in (0, -1):
        b = b'FORM' + struct.pack('>L', 4) + b'AIFC'
        b += b'COMM' + struct.pack('>LhlhhLL', 38, 1, 0, sampwidth, 16384 | 12, 11025 << 18, 0)
        b += b'NONE' + struct.pack('B', 14) + b'not compressed' + b'\x00'
        b += b'SSND' + struct.pack('>L', 8) + b'\x00' * 8
        with AIFCLowLevelTest.assertRaisesRegex(aifc.Error, 'bad sample width'):
            aifc.open(io.BytesIO(b))

AIFCLowLevelTest = test_aifc.AIFCLowLevelTest()
test_read_wrong_sample_width()
