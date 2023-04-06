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

def test_exit_exception_chaining_suppress():
    with TestBaseExitStack.exit_stack() as stack:
        stack.push(lambda *exc: True)
        stack.push(lambda *exc: 1 / 0)
        stack.push(lambda *exc: {}[1])

TestBaseExitStack = test_contextlib.TestBaseExitStack()
test_exit_exception_chaining_suppress()
