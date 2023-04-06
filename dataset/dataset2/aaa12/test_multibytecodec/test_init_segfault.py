from test import support
from test.support import os_helper
from test.support.os_helper import TESTFN
import unittest, io, codecs, sys
import _multibytecodec
import test_multibytecodec

def test_init_segfault():
    Test_MultibyteCodec.assertRaises(AttributeError, _multibytecodec.MultibyteStreamReader, None)
    Test_MultibyteCodec.assertRaises(AttributeError, _multibytecodec.MultibyteStreamWriter, None)

Test_MultibyteCodec = test_multibytecodec.Test_MultibyteCodec()
test_init_segfault()
