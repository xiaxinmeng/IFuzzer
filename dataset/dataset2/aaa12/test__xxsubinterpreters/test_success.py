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

def test_success():
    (script, file) = test__xxsubinterpreters._captured_script('print("it worked!", end="")')
    with file:
        test__xxsubinterpreters.interpreters.run_string(RunStringTests.id, script)
        out = file.read()
    RunStringTests.assertEqual(out, 'it worked!')

RunStringTests = test__xxsubinterpreters.RunStringTests()
test_success()
