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

def test_success():
    interp = interpreters.create()
    (script, file) = test_interpreters._captured_script('print("it worked!", end="")')
    with file:
        interp.run(script)
        out = file.read()
    TestInterpreterRun.assertEqual(out, 'it worked!')

TestInterpreterRun = test_interpreters.TestInterpreterRun()
test_success()
