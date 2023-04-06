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

def test_already_destroyed():
    interp = interpreters.create()
    interp.close()
    with TestInterpreterIsRunning.assertRaises(RuntimeError):
        interp.close()

TestInterpreterIsRunning = test_interpreters.TestInterpreterIsRunning()
test_already_destroyed()
