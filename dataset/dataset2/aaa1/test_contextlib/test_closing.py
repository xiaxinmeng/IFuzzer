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

def test_closing():
    state = []

    class C:

        def close(ClosingTestCase):
            state.append(1)
    x = C()
    ClosingTestCase.assertEqual(state, [])
    with closing(x) as y:
        ClosingTestCase.assertEqual(x, y)
    ClosingTestCase.assertEqual(state, [1])

ClosingTestCase = test_contextlib.ClosingTestCase()
test_closing()
