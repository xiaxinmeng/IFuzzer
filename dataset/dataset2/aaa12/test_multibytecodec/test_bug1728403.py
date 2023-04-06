from test import support
from test.support import os_helper
from test.support.os_helper import TESTFN
import unittest, io, codecs, sys
import _multibytecodec
import test_multibytecodec

def test_bug1728403():
    try:
        f = open(TESTFN, 'wb')
        try:
            f.write(b'\xa1')
        finally:
            f.close()
        f = codecs.open(TESTFN, encoding='cp949')
        try:
            Test_StreamReader.assertRaises(UnicodeDecodeError, f.read, 2)
        finally:
            f.close()
    finally:
        os_helper.unlink(TESTFN)

Test_StreamReader = test_multibytecodec.Test_StreamReader()
test_bug1728403()
