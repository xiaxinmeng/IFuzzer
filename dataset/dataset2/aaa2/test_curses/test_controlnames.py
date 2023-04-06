import os
import string
import sys
import tempfile
import unittest
from test.support import requires, verbose, SaveSignals
from test.support.import_helper import import_module
import inspect
import curses.panel
import codecs
import test_curses

def test_controlnames():
    for name in curses.ascii.controlnames:
        TestAscii.assertTrue(hasattr(curses.ascii, name), name)

TestAscii = test_curses.TestAscii()
test_controlnames()
