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

def test_error_id():
    with RunStringTests.assertRaises(ValueError):
        test__xxsubinterpreters.interpreters.run_string(-1, 'print("spam")')

RunStringTests = test__xxsubinterpreters.RunStringTests()
test_error_id()
