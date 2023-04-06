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

def test_encoding():
    stdscr = TestCurses.stdscr
    import codecs
    encoding = stdscr.encoding
    codecs.lookup(encoding)
    with TestCurses.assertRaises(TypeError):
        stdscr.encoding = 10
    stdscr.encoding = encoding
    with TestCurses.assertRaises(TypeError):
        del stdscr.encoding

TestCurses = test_curses.TestCurses()
test_encoding()
