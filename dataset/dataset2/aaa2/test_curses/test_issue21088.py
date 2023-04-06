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

def test_issue21088():
    stdscr = TestCurses.stdscr
    try:
        signature = inspect.signature(stdscr.addch)
        TestCurses.assertFalse(signature)
    except ValueError:
        pass
    human_readable_signature = stdscr.addch.__doc__.split('\n')[0]
    TestCurses.assertIn('[y, x,]', human_readable_signature)

TestCurses = test_curses.TestCurses()
test_issue21088()
