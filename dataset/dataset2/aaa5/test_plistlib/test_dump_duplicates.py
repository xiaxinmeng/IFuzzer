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

def test_dump_duplicates():
    for x in (None, False, True, 12345, 123.45, 'abcde', 'абвгд', b'abcde', datetime.datetime(2004, 10, 26, 10, 33, 33), bytearray(b'abcde'), [12, 345], (12, 345), {'12': 345}):
        with TestBinaryPlistlib.subTest(x=x):
            data = plistlib.dumps([x] * 1000, fmt=plistlib.FMT_BINARY)
            TestBinaryPlistlib.assertLess(len(data), 1100, repr(data))

TestBinaryPlistlib = test_plistlib.TestBinaryPlistlib()
test_dump_duplicates()
