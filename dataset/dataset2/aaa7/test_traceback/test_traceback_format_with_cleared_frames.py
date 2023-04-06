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

def test_traceback_format_with_cleared_frames():

    def cleanup_tb(tb):
        tb.tb_frame.clear()
    TracebackFormatTests.check_traceback_format(cleanup_tb)

TracebackFormatTests = test_traceback.TracebackFormatTests()
test_traceback_format_with_cleared_frames()
