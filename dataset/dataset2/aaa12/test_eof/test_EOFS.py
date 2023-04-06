import sys
from test import support
from test.support import os_helper
from test.support import script_helper
import unittest
import test_eof

def test_EOFS():
    expect = 'EOF while scanning triple-quoted string literal (<string>, line 1)'
    try:
        eval("'''this is a test")
    except SyntaxError as msg:
        EOFTestCase.assertEqual(str(msg), expect)
    else:
        raise support.TestFailed

EOFTestCase = test_eof.EOFTestCase()
test_EOFS()
