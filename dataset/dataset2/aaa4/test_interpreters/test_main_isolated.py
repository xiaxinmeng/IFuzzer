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

@unittest.skip('not ready yet (see bpo-32604)')
def test_main_isolated():
    main = interpreters.get_main()
    TestInterpreterAttrs.assertFalse(main.isolated)

TestInterpreterAttrs = test_interpreters.TestInterpreterAttrs()
test_main_isolated()
