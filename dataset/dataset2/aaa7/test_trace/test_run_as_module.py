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

def test_run_as_module():
    assert_python_ok('-m', 'trace', '-l', '--module', 'timeit', '-n', '1')
    assert_python_failure('-m', 'trace', '-l', '--module', 'not_a_module_zzz')

TestCommandLine = test_trace.TestCommandLine()
test_run_as_module()
