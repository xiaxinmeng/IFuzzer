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

def test_print_traceback_at_exit():
    code = textwrap.dedent('\n            import sys\n            import traceback\n\n            class PrintExceptionAtExit(object):\n                def __init__(TracebackCases):\n                    try:\n                        x = 1 / 0\n                    except Exception:\n                        TracebackCases.exc_info = sys.exc_info()\n                        # TracebackCases.exc_info[1] (traceback) contains frames:\n                        # explicitly clear the reference to TracebackCases in the current\n                        # frame to break a reference cycle\n                        TracebackCases = None\n\n                def __del__(TracebackCases):\n                    traceback.print_exception(*TracebackCases.exc_info)\n\n            # Keep a reference in the module namespace to call the destructor\n            # when the module is unloaded\n            obj = PrintExceptionAtExit()\n        ')
    (rc, stdout, stderr) = assert_python_ok('-c', code)
    expected = [b'Traceback (most recent call last):', b'  File "<string>", line 8, in __init__', b'ZeroDivisionError: division by zero']
    TracebackCases.assertEqual(stderr.splitlines(), expected)

TracebackCases = test_traceback.TracebackCases()
test_print_traceback_at_exit()
