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

def test_simple_caller():
    TestFuncs.tracer.runfunc(test_trace.traced_func_simple_caller, 1)
    expected = {TestFuncs.filemod + ('traced_func_simple_caller',): 1, TestFuncs.filemod + ('traced_func_linear',): 1}
    TestFuncs.assertEqual(TestFuncs.tracer.results().calledfuncs, expected)

TestFuncs = test_trace.TestFuncs()
TestFuncs.setUp()
test_simple_caller()
