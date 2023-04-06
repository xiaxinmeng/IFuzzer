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

def test_non_bmp_characters():
    pl = {'python': '🐍'}
    for fmt in test_plistlib.ALL_FORMATS:
        with TestPlistlib.subTest(fmt=fmt):
            data = plistlib.dumps(pl, fmt=fmt)
            TestPlistlib.assertEqual(plistlib.loads(data), pl)

TestPlistlib = test_plistlib.TestPlistlib()
test_non_bmp_characters()
