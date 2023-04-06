import os
import textwrap
import unittest
from test.support import os_helper
from test.support.script_helper import assert_python_ok
import test_lltrace

def test_lltrace_does_not_crash_on_subscript_operator():
    with open(os_helper.TESTFN, 'w') as fd:
        TestLLTrace.addCleanup(os_helper.unlink, os_helper.TESTFN)
        fd.write(textwrap.dedent("            import code\n\n            console = code.InteractiveConsole()\n            console.push('__ltrace__ = 1')\n            console.push('a = [1, 2, 3]')\n            console.push('a[0] = 1')\n            print('unreachable if bug exists')\n            "))
        assert_python_ok(os_helper.TESTFN)

TestLLTrace = test_lltrace.TestLLTrace()
test_lltrace_does_not_crash_on_subscript_operator()
