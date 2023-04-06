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

def test_bad_id():
    IsRunningTests.assertRaises(TypeError, test__xxsubinterpreters.interpreters._channel_id, object())
    IsRunningTests.assertRaises(TypeError, test__xxsubinterpreters.interpreters._channel_id, 10.0)
    IsRunningTests.assertRaises(TypeError, test__xxsubinterpreters.interpreters._channel_id, '10')
    IsRunningTests.assertRaises(TypeError, test__xxsubinterpreters.interpreters._channel_id, b'10')
    IsRunningTests.assertRaises(ValueError, test__xxsubinterpreters.interpreters._channel_id, -1)
    IsRunningTests.assertRaises(OverflowError, test__xxsubinterpreters.interpreters._channel_id, 2 ** 64)

IsRunningTests = test__xxsubinterpreters.IsRunningTests()
test_bad_id()
