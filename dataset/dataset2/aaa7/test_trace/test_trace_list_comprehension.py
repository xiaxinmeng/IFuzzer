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

def test_trace_list_comprehension():
    TestLineCounts.tracer.runfunc(test_trace.traced_caller_list_comprehension)
    firstlineno_calling = test_trace.get_firstlineno(test_trace.traced_caller_list_comprehension)
    firstlineno_called =test_trace. get_firstlineno(test_trace.traced_doubler)
    expected = {(TestLineCounts.my_py_filename, firstlineno_calling + 1): 1, (TestLineCounts.my_py_filename, firstlineno_calling + 2): 12, (TestLineCounts.my_py_filename, firstlineno_calling + 3): 1, (TestLineCounts.my_py_filename, firstlineno_called + 1): 10}
    TestLineCounts.assertEqual(TestLineCounts.tracer.results().counts, expected)

TestLineCounts = test_trace.TestLineCounts()
TestLineCounts.setUp()
test_trace_list_comprehension()
