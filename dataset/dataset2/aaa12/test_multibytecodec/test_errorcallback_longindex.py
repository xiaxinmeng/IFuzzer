from test import support
from test.support import os_helper
from test.support.os_helper import TESTFN
import unittest, io, codecs, sys
import _multibytecodec
import test_multibytecodec

def test_errorcallback_longindex():
    dec = codecs.getdecoder('euc-kr')
    myreplace = lambda exc: ('', sys.maxsize + 1)
    codecs.register_error('test.cjktest', myreplace)
    Test_MultibyteCodec.assertRaises(IndexError, dec, b'apple\x92ham\x93spam', 'test.cjktest')

Test_MultibyteCodec = test_multibytecodec.Test_MultibyteCodec()
test_errorcallback_longindex()
