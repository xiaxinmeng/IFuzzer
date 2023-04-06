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

def test_write_params_raises():
    fout = aifc.open(io.BytesIO(), 'wb')
    wrong_params = (0, 0, 0, 0, b'WRNG', '')
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.setparams, wrong_params)
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.getparams)
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.setnchannels, 0)
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.getnchannels)
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.setsampwidth, 0)
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.getsampwidth)
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.setframerate, 0)
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.getframerate)
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.setcomptype, b'WRNG', '')
    fout.aiff()
    fout.setnchannels(1)
    fout.setsampwidth(1)
    fout.setframerate(1)
    fout.setnframes(1)
    fout.writeframes(b'\x00')
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.setparams, (1, 1, 1, 1, 1, 1))
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.setnchannels, 1)
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.setsampwidth, 1)
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.setframerate, 1)
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.setnframes, 1)
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.setcomptype, b'NONE', '')
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.aiff)
    AIFCLowLevelTest.assertRaises(aifc.Error, fout.aifc)

AIFCLowLevelTest = test_aifc.AIFCLowLevelTest()
test_write_params_raises()
