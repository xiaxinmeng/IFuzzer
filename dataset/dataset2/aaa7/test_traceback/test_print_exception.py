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

def test_print_exception():
    output = StringIO()
    traceback.print_exception(Exception, Exception('projector'), None, file=output)
    TracebackCases.assertEqual(output.getvalue(), 'Exception: projector\n')

TracebackCases = test_traceback.TracebackCases()
test_print_exception()
