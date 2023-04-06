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

def test_ignored():
    jn = os.path.join
    ignore = trace._Ignore(['x', 'y.z'], [jn('foo', 'bar')])
    Test_Ignore.assertTrue(ignore.names('x.py', 'x'))
    Test_Ignore.assertFalse(ignore.names('xy.py', 'xy'))
    Test_Ignore.assertFalse(ignore.names('y.py', 'y'))
    Test_Ignore.assertTrue(ignore.names(jn('foo', 'bar', 'baz.py'), 'baz'))
    Test_Ignore.assertFalse(ignore.names(jn('bar', 'z.py'), 'z'))
    Test_Ignore.assertTrue(ignore.names(jn('bar', 'baz.py'), 'baz'))

Test_Ignore = test_trace.Test_Ignore()
test_ignored()
