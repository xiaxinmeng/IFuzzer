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

def test_bytes_for_script():
    interp = interpreters.create()
    with TestInterpreterRun.assertRaises(TypeError):
        interp.run(b'print("spam")')

TestInterpreterRun = test_interpreters.TestInterpreterRun()
test_bytes_for_script()
