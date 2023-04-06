import contextlib
import os
import sys
import tracemalloc
import unittest
from unittest.mock import patch
from test.support.script_helper import assert_python_ok, assert_python_failure, interpreter_requires_environment
from test import support
from test.support import os_helper
import _testcapi
import test_tracemalloc

def test_track_already_tracked():
    nframe = 5
    tracemalloc.start(nframe)
    TestCAPI.track()
    frames = TestCAPI.track(nframe=nframe)
    TestCAPI.assertEqual(TestCAPI.get_traceback(), tracemalloc.Traceback(frames))

TestCAPI = test_tracemalloc.TestCAPI()
TestCAPI.setUp()
test_track_already_tracked()
