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

def test_exception_hierarchy():
    with suppress(LookupError):
        'Hello'[50]

TestSuppress = test_contextlib.TestSuppress()
test_exception_hierarchy()
