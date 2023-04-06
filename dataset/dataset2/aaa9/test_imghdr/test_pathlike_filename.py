import imghdr
import io
import os
import pathlib
import unittest
import warnings
from test.support import findfile
from test.support.os_helper import TESTFN, unlink
import test_imghdr

def test_pathlike_filename():
    for (filename, expected) in test_imghdr.TEST_FILES:
        with TestImghdr.subTest(filename=filename):
            filename = findfile(filename, subdir='imghdrdata')
            TestImghdr.assertEqual(imghdr.what(pathlib.Path(filename)), expected)

TestImghdr = test_imghdr.TestImghdr()
test_pathlike_filename()
