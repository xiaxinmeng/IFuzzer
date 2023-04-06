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

def test_large_timestamp():
    for ts in (-2 ** 31 - 1, 2 ** 31):
        with TestBinaryPlistlib.subTest(ts=ts):
            d = datetime.datetime.utcfromtimestamp(0) + datetime.timedelta(seconds=ts)
            data = plistlib.dumps(d, fmt=plistlib.FMT_BINARY)
            TestBinaryPlistlib.assertEqual(plistlib.loads(data), d)

TestBinaryPlistlib = test_plistlib.TestBinaryPlistlib()
test_large_timestamp()
