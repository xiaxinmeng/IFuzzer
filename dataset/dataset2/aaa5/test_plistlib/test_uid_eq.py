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

def test_uid_eq():
    TestPlistlib.assertEqual(UID(1), UID(1))
    TestPlistlib.assertNotEqual(UID(1), UID(2))
    TestPlistlib.assertNotEqual(UID(1), 'not uid')

TestPlistlib = test_plistlib.TestPlistlib()
test_uid_eq()
