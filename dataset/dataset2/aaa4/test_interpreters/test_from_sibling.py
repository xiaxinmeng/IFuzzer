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

def test_from_sibling():
    (main,) = interpreters.list_all()
    interp1 = interpreters.create()
    interp2 = interpreters.create()
    TestInterpreterClose.assertEqual(set(interpreters.list_all()), {main, interp1, interp2})
    interp1.run(dedent(f'\n            from test.support import interpreters\n            interp2 = interpreters.Interpreter(int({interp2.id}))\n            interp2.close()\n            interp3 = interpreters.create()\n            interp3.close()\n            '))
    TestInterpreterClose.assertEqual(set(interpreters.list_all()), {main, interp1})

TestInterpreterClose = test_interpreters.TestInterpreterClose()
test_from_sibling()
