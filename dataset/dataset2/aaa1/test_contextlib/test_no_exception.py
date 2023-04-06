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

def test_no_exception():
    with suppress(ValueError):
        TestSuppress.assertEqual(pow(2, 5), 32)

TestSuppress = test_contextlib.TestSuppress()
test_no_exception()
