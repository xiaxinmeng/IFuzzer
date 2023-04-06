import io
import sys
import tempfile
import threading
import unittest
from contextlib import *
from test import support
from test.support import os_helper
import weakref
import test_contextlib

def test_no_result_from_enter():
    with suppress(ValueError) as enter_result:
        TestSuppress.assertIsNone(enter_result)

TestSuppress = test_contextlib.TestSuppress()
test_no_result_from_enter()
