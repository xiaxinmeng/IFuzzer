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

@test_hashlib.requires_blake2
def test_blake2b_vectors():
    for (msg, key, md) in test_hashlib.read_vectors('blake2b'):
        key = bytes.fromhex(key)
        HashLibTestCase.check('blake2b', msg, md, key=key)

HashLibTestCase = test_hashlib.HashLibTestCase()
test_blake2b_vectors()
