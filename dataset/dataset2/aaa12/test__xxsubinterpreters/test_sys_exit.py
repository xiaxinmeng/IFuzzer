from collections import namedtuple
import contextlib
import itertools
import os
import pickle
import sys
from textwrap import dedent
import threading
import time
import unittest
from test import support
from test.support import import_helper
from test.support import script_helper
import tempfile
import test__xxsubinterpreters

def test_sys_exit():
    with RunStringTests.assert_run_failed(SystemExit):
        test__xxsubinterpreters.interpreters.run_string(RunStringTests.id, dedent('\n                import sys\n                sys.exit()\n                '))
    with RunStringTests.assert_run_failed(SystemExit, '42'):
        test__xxsubinterpreters.interpreters.run_string(RunStringTests.id, dedent('\n                import sys\n                sys.exit(42)\n                '))

RunStringTests = test__xxsubinterpreters.RunStringTests()
test_sys_exit()
