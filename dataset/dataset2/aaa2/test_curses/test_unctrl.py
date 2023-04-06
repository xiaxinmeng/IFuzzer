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

def test_unctrl():
    unctrl = curses.ascii.unctrl
    TestAscii.assertEqual(unctrl('a'), 'a')
    TestAscii.assertEqual(unctrl('A'), 'A')
    TestAscii.assertEqual(unctrl(';'), ';')
    TestAscii.assertEqual(unctrl(' '), ' ')
    TestAscii.assertEqual(unctrl('\x7f'), '^?')
    TestAscii.assertEqual(unctrl('\n'), '^J')
    TestAscii.assertEqual(unctrl('\x00'), '^@')
    TestAscii.assertEqual(unctrl(ord('A')), 'A')
    TestAscii.assertEqual(unctrl(ord('\n')), '^J')
    TestAscii.assertEqual(unctrl('\x8a'), '!^J')
    TestAscii.assertEqual(unctrl('Á'), '!A')
    TestAscii.assertEqual(unctrl(ord('\x8a')), '!^J')
    TestAscii.assertEqual(unctrl(ord('Á')), '!A')

TestAscii = test_curses.TestAscii()
test_unctrl()
