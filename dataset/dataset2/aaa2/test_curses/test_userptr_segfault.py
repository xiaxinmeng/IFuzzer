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
def test_userptr_segfault():
    w = curses.newwin(10, 10)
    panel = curses.panel.new_panel(w)

    class A:

        def __del__(TestCurses):
            panel.set_userptr(None)
    panel.set_userptr(A())
    panel.set_userptr(None)

TestCurses = test_curses.TestCurses()
test_userptr_segfault()
