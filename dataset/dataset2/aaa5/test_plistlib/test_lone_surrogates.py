import copy
import operator
import pickle
import struct
import unittest
import plistlib
import os
import datetime
import codecs
import binascii
import collections
from test import support
from test.support import os_helper
from io import BytesIO
from plistlib import UID
import test_plistlib

def test_lone_surrogates():
    for fmt in test_plistlib.ALL_FORMATS:
        with TestPlistlib.subTest(fmt=fmt):
            with TestPlistlib.assertRaises(UnicodeEncodeError):
                plistlib.dumps('\ud8ff', fmt=fmt)
            with TestPlistlib.assertRaises(UnicodeEncodeError):
                plistlib.dumps('\udcff', fmt=fmt)

TestPlistlib = test_plistlib.TestPlistlib()
test_lone_surrogates()
