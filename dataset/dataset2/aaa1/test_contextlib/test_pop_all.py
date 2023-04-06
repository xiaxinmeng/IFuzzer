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

def test_pop_all():
    result = []
    with TestBaseExitStack.exit_stack() as stack:

        @stack.callback
        def _exit():
            result.append(3)
        TestBaseExitStack.assertIsNotNone(_exit)
        new_stack = stack.pop_all()
        result.append(1)
    result.append(2)
    new_stack.close()
    TestBaseExitStack.assertEqual(result, [1, 2, 3])

TestBaseExitStack = test_contextlib.TestBaseExitStack()
test_pop_all()
