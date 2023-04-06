import unittest
from test import support
from test.support import import_helper
import binascii
import copy
import pickle
import random
import sys
from test.support import bigmemtest, _1G, _4G
import random
import test_zlib

def test_library_version():
    VersionTestCase.assertEqual(test_zlib.zlib.ZLIB_RUNTIME_VERSION[0], test_zlib.zlib.ZLIB_VERSION[0])

VersionTestCase = test_zlib.VersionTestCase()
test_library_version()
