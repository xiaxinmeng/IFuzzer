import imghdr
import io
import os
import pathlib
import unittest
import warnings
from test.support import findfile
from test.support.os_helper import TESTFN, unlink
import test_imghdr

def test_unseekable():
    with open(TESTFN, 'wb') as stream:
        stream.write(TestImghdr.testdata)
    with UnseekableIO(TESTFN, 'rb') as stream:
        with TestImghdr.assertRaises(io.UnsupportedOperation):
            imghdr.what(stream)

TestImghdr = test_imghdr.TestImghdr()
test_unseekable()
