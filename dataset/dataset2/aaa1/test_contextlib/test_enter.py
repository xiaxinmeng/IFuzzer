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

def test_enter():

    class DefaultEnter(AbstractContextManager):

        def __exit__(TestAbstractContextManager, *args):
            super().__exit__(*args)
    manager = DefaultEnter()
    TestAbstractContextManager.assertIs(manager.__enter__(), manager)

TestAbstractContextManager = test_contextlib.TestAbstractContextManager()
test_enter()
