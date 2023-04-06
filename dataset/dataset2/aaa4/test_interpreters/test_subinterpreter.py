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
def test_subinterpreter():
    interp = interpreters.create()
    GetCurrentTests.assertFalse(interp.is_running())
    with _running(interp):
        GetCurrentTests.assertTrue(interp.is_running())
    GetCurrentTests.assertFalse(interp.is_running())

GetCurrentTests = test_interpreters.GetCurrentTests()
test_subinterpreter()
