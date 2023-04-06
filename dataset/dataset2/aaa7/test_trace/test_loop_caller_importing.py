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
def test_loop_caller_importing():
    TestFuncs.tracer.runfunc(test_trace.traced_func_importing_caller, 1)
    expected = {((os.path.splitext(trace.__file__)[0] + '.py', 'trace', 'Trace.runfunc'), TestFuncs.filemod + ('traced_func_importing_caller',)): 1, (TestFuncs.filemod + ('traced_func_simple_caller',), TestFuncs.filemod + ('traced_func_linear',)): 1, (TestFuncs.filemod + ('traced_func_importing_caller',), TestFuncs.filemod + ('traced_func_simple_caller',)): 1, (TestFuncs.filemod + ('traced_func_importing_caller',), TestFuncs.filemod + ('traced_func_importing',)): 1, (TestFuncs.filemod + ('traced_func_importing',), (test_trace.fix_ext_py(testmod.__file__), 'testmod', 'func')): 1}
    TestFuncs.assertEqual(TestFuncs.tracer.results().callers, expected)

TestFuncs = test_trace.TestFuncs()
TestFuncs.setUp()
test_loop_caller_importing()
