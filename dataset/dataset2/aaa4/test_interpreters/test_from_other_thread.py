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

def test_from_other_thread():
    interp = interpreters.create()

    def f():
        interp.close()
    t = threading.Thread(target=f)
    t.start()
    t.join()

TestInterpreterClose = test_interpreters.TestInterpreterClose()
test_from_other_thread()
