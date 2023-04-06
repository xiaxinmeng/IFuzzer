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

def test_issue13051():
    stdscr = TestCurses.stdscr
    if not hasattr(stdscr, 'resize'):
        raise unittest.SkipTest('requires curses.window.resize')
    box = curses.textpad.Textbox(stdscr, insert_mode=True)
    (lines, cols) = stdscr.getmaxyx()
    stdscr.resize(lines - 2, cols - 2)
    box._insert_printable_char('a')

TestCurses = test_curses.TestCurses()
test_issue13051()
