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

def test_close():
    result = []
    with TestBaseExitStack.exit_stack() as stack:

        @stack.callback
        def _exit():
            result.append(1)
        TestBaseExitStack.assertIsNotNone(_exit)
        stack.close()
        result.append(2)
    TestBaseExitStack.assertEqual(result, [1, 2])

TestBaseExitStack = test_contextlib.TestBaseExitStack()
test_close()
