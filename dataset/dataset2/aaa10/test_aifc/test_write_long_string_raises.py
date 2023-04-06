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

def test_write_long_string_raises():
    f = io.BytesIO()
    with AIFCLowLevelTest.assertRaises(ValueError):
        aifc._write_string(f, b'too long' * 255)

AIFCLowLevelTest = test_aifc.AIFCLowLevelTest()
test_write_long_string_raises()
