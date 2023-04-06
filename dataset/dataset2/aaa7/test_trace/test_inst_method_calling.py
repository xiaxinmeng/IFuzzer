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

@unittest.skipIf(hasattr(sys, 'gettrace') and sys.gettrace(), 'pre-existing trace function throws off measurements')
def test_inst_method_calling():
    obj = test_trace.TracedClass(20)
    TestFuncs.tracer.runfunc(obj.inst_method_calling, 1)
    expected = {TestFuncs.filemod + ('TracedClass.inst_method_calling',): 1, TestFuncs.filemod + ('TracedClass.inst_method_linear',): 1, TestFuncs.filemod + ('traced_func_linear',): 1}
    TestFuncs.assertEqual(TestFuncs.tracer.results().calledfuncs, expected)

TestFuncs = test_trace.TestFuncs()
TestFuncs.setUp()
test_inst_method_calling()
