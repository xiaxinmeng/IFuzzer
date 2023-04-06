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

def test_excessive_nesting():
    with TestBaseExitStack.exit_stack() as stack:
        for i in range(10000):
            stack.callback(int)

TestBaseExitStack = test_contextlib.TestBaseExitStack()
test_excessive_nesting()
