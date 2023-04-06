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

def test_contextmanager_no_reraise():

    @contextmanager
    def whee():
        yield
    ctx = whee()
    ctx.__enter__()
    ContextManagerTestCase.assertFalse(ctx.__exit__(TypeError, TypeError('foo'), None))

ContextManagerTestCase = test_contextlib.ContextManagerTestCase()
test_contextmanager_no_reraise()
