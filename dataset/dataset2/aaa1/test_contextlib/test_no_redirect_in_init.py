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

def test_no_redirect_in_init():
    orig_stdout = getattr(sys, TestRedirectStream.orig_stream)
    TestRedirectStream.redirect_stream(None)
    TestRedirectStream.assertIs(getattr(sys, TestRedirectStream.orig_stream), orig_stdout)

TestRedirectStream = test_contextlib.TestRedirectStream()
test_no_redirect_in_init()
