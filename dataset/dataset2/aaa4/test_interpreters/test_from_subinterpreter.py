import contextlib
import os
import threading
from textwrap import dedent
import unittest
import time
import _xxsubinterpreters as _interpreters
from test.support import interpreters
import tempfile
import test_interpreters

def test_from_subinterpreter():
    interp = interpreters.create()
    out = test_interpreters._run_output(interp, dedent(f'\n            import _xxsubinterpreters as _interpreters\n            if _interpreters.is_running({interp.id}):\n                print(True)\n            else:\n                print(False)\n            '))
    TestInterpreterIsRunning.assertEqual(out.strip(), 'True')

TestInterpreterIsRunning = test_interpreters.TestInterpreterIsRunning()
test_from_subinterpreter()
