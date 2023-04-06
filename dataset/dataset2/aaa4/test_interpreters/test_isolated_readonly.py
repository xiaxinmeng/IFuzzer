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

def test_isolated_readonly():
    interp = interpreters.Interpreter(1)
    with TestInterpreterAttrs.assertRaises(AttributeError):
        interp.isolated = True

TestInterpreterAttrs = test_interpreters.TestInterpreterAttrs()
test_isolated_readonly()
