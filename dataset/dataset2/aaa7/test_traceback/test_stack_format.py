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

def test_stack_format():
    with captured_output('stderr') as ststderr:
        traceback.print_stack(sys._getframe(1))
    stfile = StringIO()
    traceback.print_stack(sys._getframe(1), file=stfile)
    TracebackFormatTests.assertEqual(ststderr.getvalue(), stfile.getvalue())
    stfmt = traceback.format_stack(sys._getframe(1))
    TracebackFormatTests.assertEqual(ststderr.getvalue(), ''.join(stfmt))

TracebackFormatTests = test_traceback.TracebackFormatTests()
test_stack_format()
