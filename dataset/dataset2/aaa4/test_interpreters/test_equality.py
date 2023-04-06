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

def test_equality():
    (_, ch1) = interpreters.create_channel()
    (_, ch2) = interpreters.create_channel()
    TestInterpreterAttrs.assertEqual(ch1, ch1)
    TestInterpreterAttrs.assertNotEqual(ch1, ch2)

TestInterpreterAttrs = test_interpreters.TestInterpreterAttrs()
test_equality()
