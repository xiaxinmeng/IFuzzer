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

def test_default_protocol():
    with shelve.Shelf({}) as s:
        TestCase.assertEqual(s._protocol, pickle.DEFAULT_PROTOCOL)

TestCase = test_shelve.TestCase()
test_default_protocol()
