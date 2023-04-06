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

def test_nokeepref():

    class A:
        pass

    @contextmanager
    def woohoo(a, b):
        a = weakref.ref(a)
        b = weakref.ref(b)
        ContextManagerTestCase.assertIsNone(a())
        ContextManagerTestCase.assertIsNone(b())
        yield
    with woohoo(A(), b=A()):
        pass

ContextManagerTestCase = test_contextlib.ContextManagerTestCase()
test_nokeepref()
