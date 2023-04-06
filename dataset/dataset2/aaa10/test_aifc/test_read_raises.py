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

def test_read_raises():
    f = io.BytesIO(b'\x00')
    AIFCLowLevelTest.assertRaises(EOFError, aifc._read_ulong, f)
    AIFCLowLevelTest.assertRaises(EOFError, aifc._read_long, f)
    AIFCLowLevelTest.assertRaises(EOFError, aifc._read_ushort, f)
    AIFCLowLevelTest.assertRaises(EOFError, aifc._read_short, f)

AIFCLowLevelTest = test_aifc.AIFCLowLevelTest()
test_read_raises()
