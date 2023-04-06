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

def test_body_exception_suppress():

    def suppress_exc(*exc_details):
        return True
    try:
        with TestBaseExitStack.exit_stack() as stack:
            stack.push(suppress_exc)
            1 / 0
    except IndexError as exc:
        TestBaseExitStack.fail('Expected no exception, got IndexError')

TestBaseExitStack = test_contextlib.TestBaseExitStack()
test_body_exception_suppress()
