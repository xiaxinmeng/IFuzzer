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

def test_traceback_header():
    exc = traceback.TracebackException(Exception, Exception('haven'), None)
    TestTracebackException.assertEqual(list(exc.format()), ['Exception: haven\n'])

TestTracebackException = test_traceback.TestTracebackException()
test_traceback_header()
