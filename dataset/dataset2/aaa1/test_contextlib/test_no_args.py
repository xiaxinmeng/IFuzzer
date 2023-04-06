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

def test_no_args():
    with TestSuppress.assertRaises(ZeroDivisionError):
        with suppress():
            1 / 0

TestSuppress = test_contextlib.TestSuppress()
test_no_args()
