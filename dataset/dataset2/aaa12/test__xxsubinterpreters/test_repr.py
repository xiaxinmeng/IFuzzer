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

def test_repr():
    cid = test__xxsubinterpreters.interpreters._channel_id(10, force=True)
    InterpreterIDTests.assertEqual(repr(cid), 'ChannelID(10)')
    cid = test__xxsubinterpreters.interpreters._channel_id(10, send=True, force=True)
    InterpreterIDTests.assertEqual(repr(cid), 'ChannelID(10, send=True)')
    cid = test__xxsubinterpreters.interpreters._channel_id(10, recv=True, force=True)
    InterpreterIDTests.assertEqual(repr(cid), 'ChannelID(10, recv=True)')
    cid = test__xxsubinterpreters.interpreters._channel_id(10, send=True, recv=True, force=True)
    InterpreterIDTests.assertEqual(repr(cid), 'ChannelID(10)')

InterpreterIDTests = test__xxsubinterpreters.InterpreterIDTests()
test_repr()
