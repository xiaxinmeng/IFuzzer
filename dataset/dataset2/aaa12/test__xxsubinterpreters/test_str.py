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

def test_str():
    cid = test__xxsubinterpreters.interpreters._channel_id(10, force=True)
    InterpreterIDTests.assertEqual(str(cid), '10')

InterpreterIDTests = test__xxsubinterpreters.InterpreterIDTests()
test_str()
