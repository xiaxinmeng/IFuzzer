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

def test__all__():
    not_exported = {'PlistFormat', 'PLISTHEADER'}
    support.check__all__(MiscTestCase, plistlib, not_exported=not_exported)

MiscTestCase = test_plistlib.MiscTestCase()
test__all__()
