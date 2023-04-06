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

def test_from_list_edited_stack():
    s = traceback.StackSummary.from_list([('foo.py', 1, 'fred', 'line')])
    s[0] = ('foo.py', 2, 'fred', 'line')
    s2 = traceback.StackSummary.from_list(s)
    TestStack.assertEqual(['  File "foo.py", line 2, in fred\n    line\n'], s2.format())

TestStack = test_traceback.TestStack()
test_from_list_edited_stack()
