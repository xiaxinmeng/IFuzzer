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

@requires_curses_func('keyname')
def test_keyname():
    curses.keyname(13)

TestCurses = test_curses.TestCurses()
test_keyname()
