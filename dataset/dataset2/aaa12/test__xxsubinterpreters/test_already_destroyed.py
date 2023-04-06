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

def test_already_destroyed():
    id = test__xxsubinterpreters.interpreters.create()
    test__xxsubinterpreters.interpreters.destroy(id)
    with IsRunningTests.assertRaises(RuntimeError):
        test__xxsubinterpreters.interpreters.destroy(id)

IsRunningTests = test__xxsubinterpreters.IsRunningTests()
test_already_destroyed()
