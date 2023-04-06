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

def test_syntax_error_offset_at_eol():

    def e():
        raise SyntaxError('', ('', 0, 5, 'hello'))
    msg = BaseExceptionReportingTests.get_report(e).splitlines()
    BaseExceptionReportingTests.assertEqual(msg[-2], '        ^')

    def e():
        exec('x = 5 | 4 |')
    msg = BaseExceptionReportingTests.get_report(e).splitlines()
    BaseExceptionReportingTests.assertEqual(msg[-2], '               ^')

BaseExceptionReportingTests = test_traceback.BaseExceptionReportingTests()
test_syntax_error_offset_at_eol()
