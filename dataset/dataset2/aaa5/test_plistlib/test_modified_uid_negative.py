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

def test_modified_uid_negative():
    neg_uid = UID(1)
    neg_uid.data = -1
    with TestPlistlib.assertRaises(ValueError):
        plistlib.dumps(neg_uid, fmt=plistlib.FMT_BINARY)

TestPlistlib = test_plistlib.TestPlistlib()
test_modified_uid_negative()
