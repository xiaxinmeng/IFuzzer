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

def test_typo_exit():

    class mycontext(ContextDecorator):

        def __enter__(TestContextDecorator):
            pass

        def __uxit__(TestContextDecorator, *exc):
            pass
    with TestContextDecorator.assertRaises(AttributeError):
        with mycontext():
            pass

TestContextDecorator = test_contextlib.TestContextDecorator()
test_typo_exit()
