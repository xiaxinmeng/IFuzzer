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

def test_invalid_uid():
    with TestPlistlib.assertRaises(TypeError):
        UID('not an int')
    with TestPlistlib.assertRaises(ValueError):
        UID(2 ** 64)
    with TestPlistlib.assertRaises(ValueError):
        UID(-19)

TestPlistlib = test_plistlib.TestPlistlib()
test_invalid_uid()
