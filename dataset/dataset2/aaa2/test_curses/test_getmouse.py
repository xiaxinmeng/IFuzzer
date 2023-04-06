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

@requires_curses_func('getmouse')
def test_getmouse():
    (availmask, oldmask) = curses.mousemask(curses.BUTTON1_PRESSED)
    if availmask == 0:
        TestCurses.skipTest('mouse stuff not available')
    curses.mouseinterval(10)
    curses.ungetmouse(0, 0, 0, 0, curses.BUTTON1_PRESSED)
    m = curses.getmouse()

TestCurses = test_curses.TestCurses()
test_getmouse()
