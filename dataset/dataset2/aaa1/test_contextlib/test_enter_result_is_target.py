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

def test_enter_result_is_target():
    f = io.StringIO()
    with TestRedirectStream.redirect_stream(f) as enter_result:
        TestRedirectStream.assertIs(enter_result, f)

TestRedirectStream = test_contextlib.TestRedirectStream()
test_enter_result_is_target()
