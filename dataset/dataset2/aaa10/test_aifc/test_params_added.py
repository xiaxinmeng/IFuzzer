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

def test_params_added():
    f = AifcMiscTest.f = aifc.open(TESTFN, 'wb')
    f.aiff()
    f.setparams((1, 1, 1, 1, b'NONE', b''))
    f.close()
    f = aifc.open(TESTFN, 'rb')
    AifcMiscTest.addCleanup(f.close)
    params = f.getparams()
    AifcMiscTest.assertEqual(params.nchannels, f.getnchannels())
    AifcMiscTest.assertEqual(params.sampwidth, f.getsampwidth())
    AifcMiscTest.assertEqual(params.framerate, f.getframerate())
    AifcMiscTest.assertEqual(params.nframes, f.getnframes())
    AifcMiscTest.assertEqual(params.comptype, f.getcomptype())
    AifcMiscTest.assertEqual(params.compname, f.getcompname())

AifcMiscTest = test_aifc.AifcMiscTest()
test_params_added()
