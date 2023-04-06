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

@unittest.skip('Fails on FreeBSD')
def test_already_running():
    interp = interpreters.create()
    with _running(interp):
        with TestInterpreterRun.assertRaises(RuntimeError):
            interp.run('print("spam")')

TestInterpreterRun = test_interpreters.TestInterpreterRun()
test_already_running()
