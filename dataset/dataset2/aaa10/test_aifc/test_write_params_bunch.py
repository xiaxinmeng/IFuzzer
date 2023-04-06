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

def test_write_params_bunch():
    fout = aifc.open(io.BytesIO(), 'wb')
    fout.aifc()
    p = (1, 2, 3, 4, b'NONE', b'name')
    fout.setparams(p)
    AIFCLowLevelTest.assertEqual(fout.getparams(), p)
    fout.initfp(None)

AIFCLowLevelTest = test_aifc.AIFCLowLevelTest()
test_write_params_bunch()
