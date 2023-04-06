import sys
from test import support
from test.support import os_helper
from test.support import script_helper
import unittest
import test_eof

def test_EOFC():
    expect = 'EOL while scanning string literal (<string>, line 1)'
    try:
        eval("'this is a test            ")
    except SyntaxError as msg:
        EOFTestCase.assertEqual(str(msg), expect)
    else:
        raise support.TestFailed

EOFTestCase = test_eof.EOFTestCase()
test_EOFC()
