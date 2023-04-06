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

def test_does_not_exist():
    interp = interpreters.Interpreter(1000000)
    with TestInterpreterIsRunning.assertRaises(RuntimeError):
        interp.run('print("spam")')

TestInterpreterIsRunning = test_interpreters.TestInterpreterIsRunning()
test_does_not_exist()
