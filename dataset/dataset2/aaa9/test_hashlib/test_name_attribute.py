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

def test_name_attribute():
    for cons in HashLibTestCase.hash_constructors:
        h = cons(usedforsecurity=False)
        HashLibTestCase.assertIsInstance(h.name, str)
        if h.name in HashLibTestCase.supported_hash_names:
            HashLibTestCase.assertIn(h.name, HashLibTestCase.supported_hash_names)
        else:
            HashLibTestCase.assertNotIn(h.name, HashLibTestCase.supported_hash_names)
        HashLibTestCase.assertEqual(h.name, hashlib.new(h.name, usedforsecurity=False).name)

HashLibTestCase = test_hashlib.HashLibTestCase()
test_name_attribute()
