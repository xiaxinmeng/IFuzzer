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

def test_contextmanager_plain():
    state = []

    @contextmanager
    def woohoo():
        state.append(1)
        yield 42
        state.append(999)
    with woohoo() as x:
        ContextManagerTestCase.assertEqual(state, [1])
        ContextManagerTestCase.assertEqual(x, 42)
        state.append(x)
    ContextManagerTestCase.assertEqual(state, [1, 42, 999])

ContextManagerTestCase = test_contextlib.ContextManagerTestCase()
test_contextmanager_plain()
