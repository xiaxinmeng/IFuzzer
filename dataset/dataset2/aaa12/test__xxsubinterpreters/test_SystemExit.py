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

def test_SystemExit():
    with RunStringTests.assert_run_failed(SystemExit, '42'):
        test__xxsubinterpreters.interpreters.run_string(RunStringTests.id, 'raise SystemExit(42)')

RunStringTests = test__xxsubinterpreters.RunStringTests()
test_SystemExit()
