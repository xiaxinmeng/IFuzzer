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

def test_write_params_singles():
    fout = aifc.open(io.BytesIO(), 'wb')
    fout.aifc()
    fout.setnchannels(1)
    fout.setsampwidth(2)
    fout.setframerate(3)
    fout.setnframes(4)
    fout.setcomptype(b'NONE', b'name')
    AIFCLowLevelTest.assertEqual(fout.getnchannels(), 1)
    AIFCLowLevelTest.assertEqual(fout.getsampwidth(), 2)
    AIFCLowLevelTest.assertEqual(fout.getframerate(), 3)
    AIFCLowLevelTest.assertEqual(fout.getnframes(), 0)
    AIFCLowLevelTest.assertEqual(fout.tell(), 0)
    AIFCLowLevelTest.assertEqual(fout.getcomptype(), b'NONE')
    AIFCLowLevelTest.assertEqual(fout.getcompname(), b'name')
    fout.writeframes(b'\x00' * 4 * fout.getsampwidth() * fout.getnchannels())
    AIFCLowLevelTest.assertEqual(fout.getnframes(), 4)
    AIFCLowLevelTest.assertEqual(fout.tell(), 4)

AIFCLowLevelTest = test_aifc.AIFCLowLevelTest()
test_write_params_singles()
