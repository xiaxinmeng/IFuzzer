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

def test_typo_enter():

    class mycontext(ContextDecorator):

        def __unter__(TestContextDecorator):
            pass

        def __exit__(TestContextDecorator, *exc):
            pass
    with TestContextDecorator.assertRaises(AttributeError):
        with mycontext():
            pass

TestContextDecorator = test_contextlib.TestContextDecorator()
test_typo_enter()
