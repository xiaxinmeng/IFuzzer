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

def test_load_singletons():
    TestBinaryPlistlib.assertIs(TestBinaryPlistlib.decode(b'\x00'), None)
    TestBinaryPlistlib.assertIs(TestBinaryPlistlib.decode(b'\x08'), False)
    TestBinaryPlistlib.assertIs(TestBinaryPlistlib.decode(b'\t'), True)
    TestBinaryPlistlib.assertEqual(TestBinaryPlistlib.decode(b'\x0f'), b'')

TestBinaryPlistlib = test_plistlib.TestBinaryPlistlib()
test_load_singletons()
