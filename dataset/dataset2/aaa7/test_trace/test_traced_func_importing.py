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

def test_traced_func_importing():
    TestLineCounts.tracer.runfunc(test_trace.traced_func_importing, 2, 5)
    firstlineno = test_trace.get_firstlineno(test_trace.traced_func_importing)
    expected = {(TestLineCounts.my_py_filename, firstlineno + 1): 1, (test_trace.fix_ext_py(testmod.__file__), 2): 1, (test_trace.fix_ext_py(testmod.__file__), 3): 1}
    TestLineCounts.assertEqual(TestLineCounts.tracer.results().counts, expected)

TestLineCounts = test_trace.TestLineCounts()
TestLineCounts.setUp()
test_traced_func_importing()
