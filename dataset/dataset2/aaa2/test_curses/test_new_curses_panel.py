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

@requires_curses_func('panel')
def test_new_curses_panel():
    w = curses.newwin(10, 10)
    panel = curses.panel.new_panel(w)
    TestCurses.assertRaises(TypeError, type(panel))

TestCurses = test_curses.TestCurses()
test_new_curses_panel()
