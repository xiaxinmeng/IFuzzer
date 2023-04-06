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

def test_instance_bypass():

    class Example(object):
        pass
    cm = Example()
    cm.__exit__ = object()
    stack = TestBaseExitStack.exit_stack()
    TestBaseExitStack.assertRaises(AttributeError, stack.enter_context, cm)
    stack.push(cm)
    TestBaseExitStack.assertIs(stack._exit_callbacks[-1][1], cm)

TestBaseExitStack = test_contextlib.TestBaseExitStack()
test_instance_bypass()
