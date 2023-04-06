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

def test_ascii():
    ascii = curses.ascii.ascii
    TestAscii.assertEqual(ascii('Á'), 'A')
    TestAscii.assertEqual(ascii('A'), 'A')
    TestAscii.assertEqual(ascii(ord('Á')), ord('A'))

TestAscii = test_curses.TestAscii()
test_ascii()
