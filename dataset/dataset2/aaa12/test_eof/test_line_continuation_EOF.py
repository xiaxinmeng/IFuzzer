import sys
from test import support
from test.support import os_helper
from test.support import script_helper
import unittest
import test_eof

def test_line_continuation_EOF():
    """A continuation at the end of input must be an error; bpo2180."""
    expect = 'unexpected EOF while parsing (<string>, line 1)'
    with EOFTestCase.assertRaises(SyntaxError) as excinfo:
        exec('x = 5\\')
    EOFTestCase.assertEqual(str(excinfo.exception), expect)
    with EOFTestCase.assertRaises(SyntaxError) as excinfo:
        exec('\\')
    EOFTestCase.assertEqual(str(excinfo.exception), expect)

EOFTestCase = test_eof.EOFTestCase()
test_line_continuation_EOF()
