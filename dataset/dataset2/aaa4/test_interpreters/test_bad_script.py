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

def test_bad_script():
    interp = interpreters.create()
    with TestInterpreterRun.assertRaises(TypeError):
        interp.run(10)

TestInterpreterRun = test_interpreters.TestInterpreterRun()
test_bad_script()
