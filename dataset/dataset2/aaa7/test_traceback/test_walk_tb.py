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

def test_walk_tb():
    try:
        1 / 0
    except Exception:
        (_, _, tb) = sys.exc_info()
    s = list(traceback.walk_tb(tb))
    TestStack.assertEqual(len(s), 1)

TestStack = test_traceback.TestStack()
test_walk_tb()
