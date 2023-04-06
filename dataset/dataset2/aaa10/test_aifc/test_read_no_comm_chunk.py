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

def test_read_no_comm_chunk():
    b = io.BytesIO(b'FORM' + struct.pack('>L', 4) + b'AIFF')
    AIFCLowLevelTest.assertRaises(aifc.Error, aifc.open, b)

AIFCLowLevelTest = test_aifc.AIFCLowLevelTest()
test_read_no_comm_chunk()
