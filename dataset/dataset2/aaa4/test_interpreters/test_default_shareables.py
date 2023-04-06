import contextlib
import os
import threading
from textwrap import dedent
import unittest
import time
import _xxsubinterpreters as _interpreters
from test.support import interpreters
import tempfile
import test_interpreters

def test_default_shareables():
    shareables = [None, b'spam', 'spam', 10, -10]
    for obj in shareables:
        with TestIsShareable.subTest(obj):
            shareable = interpreters.is_shareable(obj)
            TestIsShareable.assertTrue(shareable)

TestIsShareable = test_interpreters.TestIsShareable()
test_default_shareables()
