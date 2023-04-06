import sys
import os
import unittest
import subprocess
from textwrap import dedent
from test.support import cpython_only, SuppressCrashReport
from test.support.script_helper import kill_python
import test_repl

def test_close_stdin():
    user_input = dedent('\n            import os\n            print("before close")\n            os.close(0)\n        ')
    prepare_repl = dedent('\n            from test.support import suppress_msvcrt_asserts\n            suppress_msvcrt_asserts()\n        ')
    process = test_repl.spawn_repl('-c', prepare_repl)
    output = process.communicate(user_input)[0]
    TestInteractiveInterpreter.assertEqual(process.returncode, 0)
    TestInteractiveInterpreter.assertIn('before close', output)

TestInteractiveInterpreter = test_repl.TestInteractiveInterpreter()
test_close_stdin()
