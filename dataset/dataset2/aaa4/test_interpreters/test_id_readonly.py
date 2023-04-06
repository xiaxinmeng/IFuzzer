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

def test_id_readonly():
    sch = interpreters.SendChannel(1)
    with TestInterpreterAttrs.assertRaises(AttributeError):
        sch.id = 2

TestInterpreterAttrs = test_interpreters.TestInterpreterAttrs()
test_id_readonly()
