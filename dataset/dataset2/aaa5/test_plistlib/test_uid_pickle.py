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

def test_uid_pickle():
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        TestPlistlib.assertEqual(pickle.loads(pickle.dumps(UID(19), protocol=proto)), UID(19))

TestPlistlib = test_plistlib.TestPlistlib()
test_uid_pickle()
