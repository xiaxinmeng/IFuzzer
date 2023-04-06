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

def test_cover_files_written_with_highlight():
    argv = '-m trace --count --missing'.split() + [TestCoverageCommandLineOutput.codefile]
    (status, stdout, stderr) = assert_python_ok(*argv)
    TestCoverageCommandLineOutput.assertTrue(os.path.exists(TestCoverageCommandLineOutput.coverfile))
    with open(TestCoverageCommandLineOutput.coverfile, encoding='iso-8859-15') as f:
        TestCoverageCommandLineOutput.assertEqual(f.read(), textwrap.dedent("                       # coding: iso-8859-15\n                    1: x = 'spœm'\n                    1: if []:\n                >>>>>>     print('unreachable')\n            "))

TestCoverageCommandLineOutput = test_trace.TestCoverageCommandLineOutput()
test_cover_files_written_with_highlight()
