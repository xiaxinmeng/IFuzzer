import imghdr
import io
import os
import pathlib
import unittest
import warnings
from test.support import findfile
from test.support.os_helper import TESTFN, unlink
import test_imghdr

def test_jumbo(h, file):
    if h.startswith(b'eggs'):
        return 'ham'

TestImghdr = test_imghdr.TestImghdr()
test_jumbo()
