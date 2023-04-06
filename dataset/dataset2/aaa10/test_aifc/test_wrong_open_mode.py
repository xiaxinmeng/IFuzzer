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

def test_wrong_open_mode():
    with AIFCLowLevelTest.assertRaises(aifc.Error):
        aifc.open(TESTFN, 'wrong_mode')

AIFCLowLevelTest = test_aifc.AIFCLowLevelTest()
test_wrong_open_mode()
