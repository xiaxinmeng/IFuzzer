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

def test_nonstandard_refs_size():
    data = b'bplist00\xd1\x00\x00\x01\x00\x00\x02QaQb\x00\x00\x08\x00\x00\x0f\x00\x00\x11\x00\x00\x00\x00\x00\x00\x03\x03\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13'
    TestBinaryPlistlib.assertEqual(plistlib.loads(data), {'a': 'b'})

TestBinaryPlistlib = test_plistlib.TestBinaryPlistlib()
test_nonstandard_refs_size()
