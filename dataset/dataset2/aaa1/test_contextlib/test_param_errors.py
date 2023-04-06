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

def test_param_errors():

    @contextmanager
    def woohoo(a, *, b):
        yield
    with ContextManagerTestCase.assertRaises(TypeError):
        woohoo()
    with ContextManagerTestCase.assertRaises(TypeError):
        woohoo(3, 5)
    with ContextManagerTestCase.assertRaises(TypeError):
        woohoo(b=3)

ContextManagerTestCase = test_contextlib.ContextManagerTestCase()
test_param_errors()
