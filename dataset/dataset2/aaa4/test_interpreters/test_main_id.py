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

def test_main_id():
    main = interpreters.get_main()
    TestInterpreterAttrs.assertEqual(main.id, 0)

TestInterpreterAttrs = test_interpreters.TestInterpreterAttrs()
test_main_id()
