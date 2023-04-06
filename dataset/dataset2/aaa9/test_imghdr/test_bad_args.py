import imghdr
import io
import os
import pathlib
import unittest
import warnings
from test.support import findfile
from test.support.os_helper import TESTFN, unlink
import test_imghdr

def test_bad_args():
    with TestImghdr.assertRaises(TypeError):
        imghdr.what()
    with TestImghdr.assertRaises(AttributeError):
        imghdr.what(None)
    with TestImghdr.assertRaises(TypeError):
        imghdr.what(TestImghdr.testfile, 1)
    with TestImghdr.assertRaises(AttributeError):
        imghdr.what(os.fsencode(TestImghdr.testfile))
    with open(TestImghdr.testfile, 'rb') as f:
        with TestImghdr.assertRaises(AttributeError):
            imghdr.what(f.fileno())

TestImghdr = test_imghdr.TestImghdr()
TestImghdr.setUp()
test_bad_args()
