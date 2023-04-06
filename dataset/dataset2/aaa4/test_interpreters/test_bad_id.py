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

def test_bad_id():
    interp = interpreters.Interpreter(-1)
    with TestInterpreterIsRunning.assertRaises(ValueError):
        interp.run('print("spam")')

TestInterpreterIsRunning = test_interpreters.TestInterpreterIsRunning()
test_bad_id()
