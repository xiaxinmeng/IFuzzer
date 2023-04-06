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

def test_exit_is_abstract():

    class MissingExit(AbstractContextManager):
        pass
    with TestAbstractContextManager.assertRaises(TypeError):
        MissingExit()

TestAbstractContextManager = test_contextlib.TestAbstractContextManager()
test_exit_is_abstract()
