import imghdr
import io
import os
import pathlib
import unittest
import warnings
from test.support import findfile
from test.support.os_helper import TESTFN, unlink
import test_imghdr

def test_missing_file():
    with TestImghdr.assertRaises(FileNotFoundError):
        imghdr.what('missing')

TestImghdr = test_imghdr.TestImghdr()
test_missing_file()
