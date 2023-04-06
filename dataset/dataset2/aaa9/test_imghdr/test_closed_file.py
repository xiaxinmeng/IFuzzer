import imghdr
import io
import os
import pathlib
import unittest
import warnings
from test.support import findfile
from test.support.os_helper import TESTFN, unlink
import test_imghdr

def test_closed_file():
    stream = open(TestImghdr.testfile, 'rb')
    stream.close()
    with TestImghdr.assertRaises(ValueError) as cm:
        imghdr.what(stream)
    stream = io.BytesIO(TestImghdr.testdata)
    stream.close()
    with TestImghdr.assertRaises(ValueError) as cm:
        imghdr.what(stream)

TestImghdr = test_imghdr.TestImghdr()
test_closed_file()
