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

def test_alt():
    alt = curses.ascii.alt
    TestAscii.assertEqual(alt('\n'), '\x8a')
    TestAscii.assertEqual(alt('A'), 'Á')
    TestAscii.assertEqual(alt(ord('A')), 193)

TestAscii = test_curses.TestAscii()
test_alt()
