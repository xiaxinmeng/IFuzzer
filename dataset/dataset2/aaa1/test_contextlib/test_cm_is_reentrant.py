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

def test_cm_is_reentrant():
    ignore_exceptions = suppress(Exception)
    with ignore_exceptions:
        pass
    with ignore_exceptions:
        len(5)
    with ignore_exceptions:
        with ignore_exceptions:
            len(5)
        outer_continued = True
        1 / 0
    TestRedirectStream.assertTrue(outer_continued)

TestRedirectStream = test_contextlib.TestRedirectStream()
test_cm_is_reentrant()
