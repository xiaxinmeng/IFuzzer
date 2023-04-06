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
def test_still_running():
    (main,) = interpreters.list_all()
    interp = interpreters.create()
    with _running(interp):
        with TestInterpreterClose.assertRaises(RuntimeError):
            interp.close()
        TestInterpreterClose.assertTrue(interp.is_running())

TestInterpreterClose = test_interpreters.TestInterpreterClose()
test_still_running()
