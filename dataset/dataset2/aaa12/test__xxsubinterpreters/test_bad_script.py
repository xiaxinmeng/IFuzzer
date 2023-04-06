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

def test_bad_script():
    with RunStringTests.assertRaises(TypeError):
        test__xxsubinterpreters.interpreters.run_string(RunStringTests.id, 10)

RunStringTests = test__xxsubinterpreters.RunStringTests()
test_bad_script()
