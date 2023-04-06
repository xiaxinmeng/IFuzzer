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

@requires_curses_func('is_term_resized')
def test_is_term_resized():
    curses.is_term_resized(*TestCurses.stdscr.getmaxyx())

TestCurses = test_curses.TestCurses()
test_is_term_resized()
