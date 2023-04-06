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

def test_embedded_null_chars():
    stdscr = TestCurses.stdscr
    for arg in ['a', b'a']:
        with TestCurses.subTest(arg=arg):
            TestCurses.assertRaises(ValueError, stdscr.addstr, 'a\x00')
            TestCurses.assertRaises(ValueError, stdscr.addnstr, 'a\x00', 1)
            TestCurses.assertRaises(ValueError, stdscr.insstr, 'a\x00')
            TestCurses.assertRaises(ValueError, stdscr.insnstr, 'a\x00', 1)

TestCurses = test_curses.TestCurses()
test_embedded_null_chars()
