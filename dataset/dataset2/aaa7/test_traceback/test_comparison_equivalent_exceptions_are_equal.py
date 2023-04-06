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

def test_comparison_equivalent_exceptions_are_equal():
    excs = []
    for _ in range(2):
        try:
            1 / 0
        except:
            excs.append(traceback.TracebackException(*sys.exc_info()))
    TestTracebackException.assertEqual(excs[0], excs[1])
    TestTracebackException.assertEqual(list(excs[0].format()), list(excs[1].format()))

TestTracebackException = test_traceback.TestTracebackException()
test_comparison_equivalent_exceptions_are_equal()
