import imghdr
import io
import os
import pathlib
import unittest
import warnings
from test.support import findfile
from test.support.os_helper import TESTFN, unlink
import test_imghdr

def test_register_test():

    def test_jumbo(h, file):
        if h.startswith(b'eggs'):
            return 'ham'
    imghdr.tests.append(test_jumbo)
    TestImghdr.addCleanup(imghdr.tests.pop)
    TestImghdr.assertEqual(imghdr.what(None, b'eggs'), 'ham')

TestImghdr = test_imghdr.TestImghdr()
test_register_test()
