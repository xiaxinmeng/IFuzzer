import sys
from test import support
from test.support import os_helper
from test.support import script_helper
import unittest
import test_eof

def test_eof_with_line_continuation():
    expect = 'unexpected EOF while parsing (<string>, line 1)'
    try:
        compile('"\\xhh" \\', '<string>', 'exec', dont_inherit=True)
    except SyntaxError as msg:
        EOFTestCase.assertEqual(str(msg), expect)
    else:
        raise support.TestFailed

EOFTestCase = test_eof.EOFTestCase()
test_eof_with_line_continuation()
