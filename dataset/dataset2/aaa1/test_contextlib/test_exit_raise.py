import io
import sys
import tempfile
import threading
import unittest
from contextlib import *
from test import support
from test.support import os_helper
import weakref
import test_contextlib

def test_exit_raise():
    with TestBaseExitStack.assertRaises(ZeroDivisionError):
        with TestBaseExitStack.exit_stack() as stack:
            stack.push(lambda *exc: False)
            1 / 0

TestBaseExitStack = test_contextlib.TestBaseExitStack()
test_exit_raise()
