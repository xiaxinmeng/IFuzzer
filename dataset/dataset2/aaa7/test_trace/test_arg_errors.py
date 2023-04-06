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

def test_arg_errors():
    res = TestFuncs.tracer.runfunc(test_trace.traced_capturer, 1, 2, TestFuncs=3, func=4)
    TestFuncs.assertEqual(res, ((1, 2), {'TestFuncs': 3, 'func': 4}))
    with TestFuncs.assertRaises(TypeError):
        TestFuncs.tracer.runfunc(func=test_trace.traced_capturer, arg=1)
    with TestFuncs.assertRaises(TypeError):
        TestFuncs.tracer.runfunc()

TestFuncs = test_trace.TestFuncs()
TestFuncs.setUp()
test_arg_errors()
