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

def test_modified_uid_huge():
    huge_uid = UID(1)
    huge_uid.data = 2 ** 64
    with TestPlistlib.assertRaises(OverflowError):
        plistlib.dumps(huge_uid, fmt=plistlib.FMT_BINARY)

TestPlistlib = test_plistlib.TestPlistlib()
test_modified_uid_huge()
