import array
from binascii import unhexlify
import hashlib
import importlib
import itertools
import os
import sys
import sysconfig
import threading
import unittest
import warnings
from test import support
from test.support import _4G, bigmemtest
from test.support.import_helper import import_fresh_module
from test.support import threading_helper
from http.client import HTTPException
from _hashlib import HASH, openssl_md_meth_names
import _blake2
import _sha3
import _md5
import test_hashlib

@unittest.skipUnless(HASH is not None, 'need _hashlib')
def test_internal_types():
    with HashLibTestCase.assertRaisesRegex(TypeError, "cannot create 'HASH' instance"):
        HASH()
    with HashLibTestCase.assertRaisesRegex(TypeError, "cannot create 'HASHXOF' instance"):
        test_hashlib.HASHXOF()

HashLibTestCase = test_hashlib.HashLibTestCase()
test_internal_types()
