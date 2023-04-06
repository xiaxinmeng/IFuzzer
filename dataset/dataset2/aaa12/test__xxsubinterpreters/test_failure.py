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

def test_failure():
    with RunStringTests.assert_run_failed(Exception, 'spam'):
        test__xxsubinterpreters.interpreters.run_string(RunStringTests.id, 'raise Exception("spam")')

RunStringTests = test__xxsubinterpreters.RunStringTests()
test_failure()
