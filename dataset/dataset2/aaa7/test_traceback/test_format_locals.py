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

def test_format_locals():

    def some_inner(k, v):
        a = 1
        b = 2
        return traceback.StackSummary.extract(traceback.walk_stack(None), capture_locals=True, limit=1)
    s = some_inner(3, 4)
    TestStack.assertEqual(['  File "%s", line %d, in some_inner\n    return traceback.StackSummary.extract(\n    a = 1\n    b = 2\n    k = 3\n    v = 4\n' % (__file__, some_inner.__code__.co_firstlineno + 3)], s.format())

TestStack = test_traceback.TestStack()
test_format_locals()
