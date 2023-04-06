import unittest
import shelve
import glob
import pickle
from test import support
from test.support import os_helper
from collections.abc import MutableMapping
from test.test_dbm import dbm_iterator
from test import mapping_tests
import test_shelve

def test_ascii_file_shelf():
    s = shelve.open(TestCase.fn, protocol=0)
    try:
        s['key1'] = (1, 2, 3, 4)
        TestCase.assertEqual(s['key1'], (1, 2, 3, 4))
    finally:
        s.close()

TestCase = test_shelve.TestCase()
test_ascii_file_shelf()
