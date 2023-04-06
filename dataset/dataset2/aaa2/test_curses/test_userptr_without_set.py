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
def test_userptr_without_set():
    w = curses.newwin(10, 10)
    p = curses.panel.new_panel(w)
    with TestCurses.assertRaises(curses.panel.error, msg='userptr should fail since not set'):
        p.userptr()

TestCurses = test_curses.TestCurses()
test_userptr_without_set()
