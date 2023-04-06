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

def test_no_resources():
    with TestBaseExitStack.exit_stack():
        pass

TestBaseExitStack = test_contextlib.TestBaseExitStack()
test_no_resources()
