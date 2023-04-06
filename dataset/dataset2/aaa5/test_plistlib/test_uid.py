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

def test_uid():
    data = UID(1)
    TestPlistlib.assertEqual(plistlib.loads(plistlib.dumps(data, fmt=plistlib.FMT_BINARY)), data)
    dict_data = {'uid0': UID(0), 'uid2': UID(2), 'uid8': UID(2 ** 8), 'uid16': UID(2 ** 16), 'uid32': UID(2 ** 32), 'uid63': UID(2 ** 63)}
    TestPlistlib.assertEqual(plistlib.loads(plistlib.dumps(dict_data, fmt=plistlib.FMT_BINARY)), dict_data)

TestPlistlib = test_plistlib.TestPlistlib()
test_uid()
