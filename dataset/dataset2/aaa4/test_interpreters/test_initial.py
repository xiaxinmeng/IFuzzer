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

def test_initial():
    interps = interpreters.list_all()
    ListAllTests.assertEqual(1, len(interps))

ListAllTests = test_interpreters.ListAllTests()
test_initial()
