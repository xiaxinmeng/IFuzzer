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

def test_from_current():
    (main,) = interpreters.list_all()
    interp = interpreters.create()
    out = test_interpreters._run_output(interp, dedent(f"\n            from test.support import interpreters\n            interp = interpreters.Interpreter({int(interp.id)})\n            try:\n                interp.close()\n            except RuntimeError:\n                print('failed')\n            "))
    TestInterpreterClose.assertEqual(out.strip(), 'failed')
    TestInterpreterClose.assertEqual(set(interpreters.list_all()), {main, interp})

TestInterpreterClose = test_interpreters.TestInterpreterClose()

test_from_current()
