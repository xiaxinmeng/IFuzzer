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

def test_ctrl():
    ctrl = curses.ascii.ctrl
    TestAscii.assertEqual(ctrl('J'), '\n')
    TestAscii.assertEqual(ctrl('\n'), '\n')
    TestAscii.assertEqual(ctrl('@'), '\x00')
    TestAscii.assertEqual(ctrl(ord('J')), ord('\n'))

TestAscii = test_curses.TestAscii()
test_ctrl()
