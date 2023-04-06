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

@requires_curses_func('update_lines_cols')
def test_update_lines_cols():
    curses.update_lines_cols()

MiscTests = test_curses.MiscTests()
test_update_lines_cols()
