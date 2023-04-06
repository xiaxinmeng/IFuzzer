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

def test_custom_isolated_explicit():
    interp1 = interpreters.Interpreter(1, isolated=True)
    interp2 = interpreters.Interpreter(1, isolated=False)
    TestInterpreterAttrs.assertTrue(interp1.isolated)
    TestInterpreterAttrs.assertFalse(interp2.isolated)

TestInterpreterAttrs = test_interpreters.TestInterpreterAttrs()
test_custom_isolated_explicit()
