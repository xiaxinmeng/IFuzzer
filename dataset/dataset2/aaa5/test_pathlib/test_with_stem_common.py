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

def test_with_stem_common():
    P = _BasePurePathTest.cls
    _BasePurePathTest.assertEqual(P('a/b').with_stem('d'), P('a/d'))
    _BasePurePathTest.assertEqual(P('/a/b').with_stem('d'), P('/a/d'))
    _BasePurePathTest.assertEqual(P('a/b.py').with_stem('d'), P('a/d.py'))
    _BasePurePathTest.assertEqual(P('/a/b.py').with_stem('d'), P('/a/d.py'))
    _BasePurePathTest.assertEqual(P('/a/b.tar.gz').with_stem('d'), P('/a/d.gz'))
    _BasePurePathTest.assertEqual(P('a/Dot ending.').with_stem('d'), P('a/d'))
    _BasePurePathTest.assertEqual(P('/a/Dot ending.').with_stem('d'), P('/a/d'))
    _BasePurePathTest.assertRaises(ValueError, P('').with_stem, 'd')
    _BasePurePathTest.assertRaises(ValueError, P('.').with_stem, 'd')
    _BasePurePathTest.assertRaises(ValueError, P('/').with_stem, 'd')
    _BasePurePathTest.assertRaises(ValueError, P('a/b').with_stem, '')
    _BasePurePathTest.assertRaises(ValueError, P('a/b').with_stem, '/c')
    _BasePurePathTest.assertRaises(ValueError, P('a/b').with_stem, 'c/')
    _BasePurePathTest.assertRaises(ValueError, P('a/b').with_stem, 'c/d')

_BasePurePathTest = test_pathlib._BasePurePathTest()
test_with_stem_common()
