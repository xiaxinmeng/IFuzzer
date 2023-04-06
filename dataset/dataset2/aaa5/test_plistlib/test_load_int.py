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

def test_load_int():
    TestBinaryPlistlib.assertEqual(TestBinaryPlistlib.decode(b'\x10\x00'), 0)
    TestBinaryPlistlib.assertEqual(TestBinaryPlistlib.decode(b'\x10\xfe'), 254)
    TestBinaryPlistlib.assertEqual(TestBinaryPlistlib.decode(b'\x11\xfe\xdc'), 65244)
    TestBinaryPlistlib.assertEqual(TestBinaryPlistlib.decode(b'\x12\xfe\xdc\xba\x98'), 4275878552)
    TestBinaryPlistlib.assertEqual(TestBinaryPlistlib.decode(b'\x13\x01#Eg\x89\xab\xcd\xef'), 81985529216486895)
    TestBinaryPlistlib.assertEqual(TestBinaryPlistlib.decode(b'\x13\xfe\xdc\xba\x98vT2\x10'), -81985529216486896)

TestBinaryPlistlib = test_plistlib.TestBinaryPlistlib()
test_load_int()
