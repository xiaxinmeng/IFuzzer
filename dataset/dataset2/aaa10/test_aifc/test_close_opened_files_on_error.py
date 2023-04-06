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

def test_close_opened_files_on_error():
    non_aifc_file = findfile('pluck-pcm8.wav', subdir='audiodata')
    with check_no_resource_warning(AifcMiscTest):
        with AifcMiscTest.assertRaises(aifc.Error):
            AifcMiscTest.f = aifc.open(non_aifc_file, 'rb')
        with mock.patch.object(aifc.Aifc_write, 'initfp', side_effect=RuntimeError):
            with AifcMiscTest.assertRaises(RuntimeError):
                AifcMiscTest.fout = aifc.open(TESTFN, 'wb')

AifcMiscTest = test_aifc.AifcMiscTest()
test_close_opened_files_on_error()
