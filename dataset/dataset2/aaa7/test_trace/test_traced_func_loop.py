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

def test_traced_func_loop():
    TestLineCounts.tracer.runfunc(test_trace.traced_func_loop, 2, 3)
    firstlineno = test_trace.get_firstlineno(test_trace.traced_func_loop)
    expected = {(TestLineCounts.my_py_filename, firstlineno + 1): 1, (TestLineCounts.my_py_filename, firstlineno + 2): 6, (TestLineCounts.my_py_filename, firstlineno + 3): 5, (TestLineCounts.my_py_filename, firstlineno + 4): 1}
    TestLineCounts.assertEqual(TestLineCounts.tracer.results().counts, expected)

TestLineCounts = test_trace.TestLineCounts()
TestLineCounts.setUp()
test_traced_func_loop()
