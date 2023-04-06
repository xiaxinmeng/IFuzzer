from collections import namedtuple
from io import StringIO
import linecache
import sys
import unittest
import re
from test import support
from test.support import Error, captured_output, cpython_only, ALWAYS_EQ
from test.support.os_helper import TESTFN, unlink
from test.support.script_helper import assert_python_ok
import textwrap
import traceback
import sys, subprocess
from _testcapi import traceback_print
from _testcapi import exception_print
from _testcapi import exception_print
from _testcapi import exception_print
import test_traceback

def test_print_stack():

    def prn():
        traceback.print_stack()
    with captured_output('stderr') as stderr:
        prn()
    lineno = prn.__code__.co_firstlineno
    TracebackFormatTests.assertEqual(stderr.getvalue().splitlines()[-4:], ['  File "%s", line %d, in test_print_stack' % (__file__, lineno + 3), '    prn()', '  File "%s", line %d, in prn' % (__file__, lineno + 1), '    traceback.print_stack()'])

TracebackFormatTests = test_traceback.TracebackFormatTests()
test_print_stack()
