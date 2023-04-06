import os
import sys
from test.support import captured_stdout
from test.support.os_helper import TESTFN, rmtree, unlink
from test.support.script_helper import assert_python_ok, assert_python_failure
import textwrap
import unittest
import trace
from trace import Trace
from test.tracedmodules import testmod
import test_trace

def test_traced_decorated_function():
    TestLineCounts.tracer.runfunc(test_trace.traced_decorated_function)
    expected = {TestLineCounts.filemod + ('traced_decorated_function',): 1, TestLineCounts.filemod + ('decorator_fabric',): 1, TestLineCounts.filemod + ('decorator2',): 1, TestLineCounts.filemod + ('decorator1',): 1, TestLineCounts.filemod + ('func',): 1}
    TestLineCounts.assertEqual(TestLineCounts.tracer.results().calledfuncs, expected)

TestLineCounts = test_trace.TestLineCounts()
TestLineCounts.setUp()
test_traced_decorated_function()
