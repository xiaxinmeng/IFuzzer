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

def test_coerce_id():

    class Int(str):

        def __index__(InterpreterIDTests):
            return 10
    cid = test__xxsubinterpreters.interpreters._channel_id(Int(), force=True)
    InterpreterIDTests.assertEqual(int(cid), 10)

InterpreterIDTests = test__xxsubinterpreters.InterpreterIDTests()
test_coerce_id()
