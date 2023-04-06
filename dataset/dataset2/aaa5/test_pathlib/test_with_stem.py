import collections.abc
import io
import os
import sys
import errno
import pathlib
import pickle
import socket
import stat
import tempfile
import unittest
from unittest import mock
from test.support import import_helper
from test.support import os_helper
from test.support.os_helper import TESTFN, FakePath
import grp, pwd
from urllib.parse import quote_from_bytes
import pwd
import test_pathlib

def test_with_stem():
    P = PureWindowsPathTest.cls
    PureWindowsPathTest.assertEqual(P('c:a/b').with_stem('d'), P('c:a/d'))
    PureWindowsPathTest.assertEqual(P('c:/a/b').with_stem('d'), P('c:/a/d'))
    PureWindowsPathTest.assertEqual(P('c:a/Dot ending.').with_stem('d'), P('c:a/d'))
    PureWindowsPathTest.assertEqual(P('c:/a/Dot ending.').with_stem('d'), P('c:/a/d'))
    PureWindowsPathTest.assertRaises(ValueError, P('c:').with_stem, 'd')
    PureWindowsPathTest.assertRaises(ValueError, P('c:/').with_stem, 'd')
    PureWindowsPathTest.assertRaises(ValueError, P('//My/Share').with_stem, 'd')
    PureWindowsPathTest.assertRaises(ValueError, P('c:a/b').with_stem, 'd:')
    PureWindowsPathTest.assertRaises(ValueError, P('c:a/b').with_stem, 'd:e')
    PureWindowsPathTest.assertRaises(ValueError, P('c:a/b').with_stem, 'd:/e')
    PureWindowsPathTest.assertRaises(ValueError, P('c:a/b').with_stem, '//My/Share')

PureWindowsPathTest = test_pathlib.PureWindowsPathTest()
test_with_stem()
