import imghdr
import io
import os
import pathlib
import unittest
import warnings
from test.support import findfile
from test.support.os_helper import TESTFN, unlink
import test_imghdr

def test_invalid_headers():
    for header in (b'\x89PN\r\n', b'\x01\xd9', b'Y\xa6', b'cutecat', b'000000JFI', b'GIF80'):
        TestImghdr.assertIsNone(imghdr.what(None, header))

TestImghdr = test_imghdr.TestImghdr()
test_invalid_headers()
