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

def test_contextmanager_trap_yield_after_throw():

    @contextmanager
    def whoo():
        try:
            yield
        except:
            yield
    ctx = whoo()
    ctx.__enter__()
    ContextManagerTestCase.assertRaises(RuntimeError, ctx.__exit__, TypeError, TypeError('foo'), None)

ContextManagerTestCase = test_contextlib.ContextManagerTestCase()
test_contextmanager_trap_yield_after_throw()
