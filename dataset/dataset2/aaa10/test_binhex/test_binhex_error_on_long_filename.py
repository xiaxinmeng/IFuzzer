import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
from test.support import warnings_helper
import test_binhex

def test_binhex_error_on_long_filename():
    """
        The testcase fails if no exception is raised when a filename parameter provided to binhex.binhex()
        is too long, or if the exception raised in binhex.binhex() is not an instance of binhex.Error.
        """
    f3 = open(BinHexTestCase.fname3, 'wb')
    f3.close()
    BinHexTestCase.assertRaises(test_binhex.binhex.Error, test_binhex.binhex.binhex, BinHexTestCase.fname3, BinHexTestCase.fname2)

BinHexTestCase = test_binhex.BinHexTestCase()
BinHexTestCase.setUp()
test_binhex_error_on_long_filename()
