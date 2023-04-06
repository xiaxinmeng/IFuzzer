import imghdr
import io
import os
import pathlib
import unittest
import warnings
from test.support import findfile
from test.support.os_helper import TESTFN, unlink
import test_imghdr

def test_file_pos():
    with open(TESTFN, 'wb') as stream:
        stream.write(b'ababagalamaga')
        pos = stream.tell()
        stream.write(TestImghdr.testdata)
    with open(TESTFN, 'rb') as stream:
        stream.seek(pos)
        TestImghdr.assertEqual(imghdr.what(stream), 'png')
        TestImghdr.assertEqual(stream.tell(), pos)

TestImghdr = test_imghdr.TestImghdr()
test_file_pos()
