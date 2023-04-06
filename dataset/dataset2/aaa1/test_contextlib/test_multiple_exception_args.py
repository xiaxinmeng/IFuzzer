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

def test_multiple_exception_args():
    with suppress(ZeroDivisionError, TypeError):
        1 / 0
    with suppress(ZeroDivisionError, TypeError):
        len(5)

TestSuppress = test_contextlib.TestSuppress()
test_multiple_exception_args()
