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

def test_invalid_binary():
    for (name, data) in test_plistlib.INVALID_BINARY_PLISTS:
        with TestBinaryPlistlib.subTest(name):
            with TestBinaryPlistlib.assertRaises(plistlib.InvalidFileException):
                plistlib.loads(b'bplist00' + data, fmt=plistlib.FMT_BINARY)

TestBinaryPlistlib = test_plistlib.TestBinaryPlistlib()
test_invalid_binary()
