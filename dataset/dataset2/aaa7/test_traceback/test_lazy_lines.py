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

def test_lazy_lines():
    linecache.clearcache()
    f = traceback.FrameSummary('f', 1, 'dummy', lookup_line=False)
    TestFrame.assertEqual(None, f._line)
    linecache.lazycache('f', globals())
    TestFrame.assertEqual('"""Test cases for traceback module"""', f.line)

TestFrame = test_traceback.TestFrame()
test_lazy_lines()
