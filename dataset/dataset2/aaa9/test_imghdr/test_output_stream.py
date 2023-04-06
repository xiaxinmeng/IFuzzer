import imghdr
import io
import os
import pathlib
import unittest
import warnings
from test.support import findfile
from test.support.os_helper import TESTFN, unlink
import test_imghdr

def test_output_stream():
    with open(TESTFN, 'wb') as stream:
        stream.write(TestImghdr.testdata)
        stream.seek(0)
        with TestImghdr.assertRaises(OSError) as cm:
            imghdr.what(stream)

TestImghdr = test_imghdr.TestImghdr()
test_output_stream()
