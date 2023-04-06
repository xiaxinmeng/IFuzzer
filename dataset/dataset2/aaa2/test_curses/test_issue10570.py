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

def test_issue10570():
    b = curses.tparm(curses.tigetstr('cup'), 5, 3)
    TestCurses.assertIs(type(b), bytes)

TestCurses = test_curses.TestCurses()
test_issue10570()
