import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
from test.support import warnings_helper
import test_binhex

def test_binhex_line_endings():
    with open(BinHexTestCase.fname1, 'wb') as f:
        f.write(BinHexTestCase.DATA)
    test_binhex.binhex.binhex(BinHexTestCase.fname1, BinHexTestCase.fname2)
    with open(BinHexTestCase.fname2, 'rb') as fp:
        contents = fp.read()
    BinHexTestCase.assertNotIn(b'\n', contents)

BinHexTestCase = test_binhex.BinHexTestCase()
BinHexTestCase.setUp()
test_binhex_line_endings()
