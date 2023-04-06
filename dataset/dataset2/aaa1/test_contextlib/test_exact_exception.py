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

def test_exact_exception():
    with suppress(TypeError):
        len(5)

TestSuppress = test_contextlib.TestSuppress()
test_exact_exception()
