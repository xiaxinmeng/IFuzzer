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

def test_custom_id():
    sch = interpreters.SendChannel(1)
    TestInterpreterAttrs.assertEqual(sch.id, 1)
    with TestInterpreterAttrs.assertRaises(TypeError):
        interpreters.SendChannel('1')

TestInterpreterAttrs = test_interpreters.TestInterpreterAttrs()
test_custom_id()
