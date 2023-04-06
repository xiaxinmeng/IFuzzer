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
from _hashlib import HASH,  openssl_md_meth_names
import _blake2
import _sha3
import _md5
import test_hashlib

def test_hexdigest():
    for cons in HashLibTestCase.hash_constructors:
        h = cons(usedforsecurity=False)
        if h.name in HashLibTestCase.shakes:
            HashLibTestCase.assertIsInstance(h.digest(16), bytes)
            HashLibTestCase.assertEqual(test_hashlib.hexstr(h.digest(16)), h.hexdigest(16))
        else:
            HashLibTestCase.assertIsInstance(h.digest(), bytes)
            HashLibTestCase.assertEqual(test_hashlib.hexstr(h.digest()), h.hexdigest())

HashLibTestCase = test_hashlib.HashLibTestCase()
test_hexdigest()
