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

@cpython_only
def test_recursive_traceback_cpython_internal():
    from _testcapi import exception_print

    def render_exc():
        (exc_type, exc_value, exc_tb) = sys.exc_info()
        exception_print(exc_value)
    TracebackFormatTests._check_recursive_traceback_display(render_exc)

TracebackFormatTests = test_traceback.TracebackFormatTests()
test_recursive_traceback_cpython_internal()
