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

def test_in_main():
    interp = interpreters.create()
    CreateTests.assertIsInstance(interp, interpreters.Interpreter)
    CreateTests.assertIn(interp, interpreters.list_all())

CreateTests = test_interpreters.CreateTests()
test_in_main()
