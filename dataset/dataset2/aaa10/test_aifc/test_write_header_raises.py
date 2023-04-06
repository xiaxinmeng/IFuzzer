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

def test_write_header_raises():
    fout = aifc.open(io.BytesIO(), 'wb')
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.close)
    fout = aifc.open(io.BytesIO(), 'wb')
    fout.setnchannels(1)
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.close)
    fout = aifc.open(io.BytesIO(), 'wb')
    fout.setnchannels(1)
    fout.setsampwidth(1)
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.close)

AIFCLowLevelTest = test_aifc.AIFCLowLevelTest()
test_write_header_raises()
