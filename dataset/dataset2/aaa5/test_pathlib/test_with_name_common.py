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

def test_with_name_common():
    P = _BasePurePathTest.cls
    _BasePurePathTest.assertEqual(P('a/b').with_name('d.xml'), P('a/d.xml'))
    _BasePurePathTest.assertEqual(P('/a/b').with_name('d.xml'), P('/a/d.xml'))
    _BasePurePathTest.assertEqual(P('a/b.py').with_name('d.xml'), P('a/d.xml'))
    _BasePurePathTest.assertEqual(P('/a/b.py').with_name('d.xml'), P('/a/d.xml'))
    _BasePurePathTest.assertEqual(P('a/Dot ending.').with_name('d.xml'), P('a/d.xml'))
    _BasePurePathTest.assertEqual(P('/a/Dot ending.').with_name('d.xml'), P('/a/d.xml'))
    _BasePurePathTest.assertRaises(ValueError, P('').with_name, 'd.xml')
    _BasePurePathTest.assertRaises(ValueError, P('.').with_name, 'd.xml')
    _BasePurePathTest.assertRaises(ValueError, P('/').with_name, 'd.xml')
    _BasePurePathTest.assertRaises(ValueError, P('a/b').with_name, '')
    _BasePurePathTest.assertRaises(ValueError, P('a/b').with_name, '/c')
    _BasePurePathTest.assertRaises(ValueError, P('a/b').with_name, 'c/')
    _BasePurePathTest.assertRaises(ValueError, P('a/b').with_name, 'c/d')

_BasePurePathTest = test_pathlib._BasePurePathTest()
test_with_name_common()
