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

@unittest.skip('Fails on FreeBSD')
def test_subinterpreter():
    interp = test__xxsubinterpreters.interpreters.create()
    GetCurrentTests.assertFalse(test__xxsubinterpreters.interpreters.is_running(interp))
    with test__xxsubinterpreters._running(interp):
        GetCurrentTests.assertTrue(test__xxsubinterpreters.interpreters.is_running(interp))
    GetCurrentTests.assertFalse(test__xxsubinterpreters.interpreters.is_running(interp))

GetCurrentTests = test__xxsubinterpreters.GetCurrentTests()
test_subinterpreter()
