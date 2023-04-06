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

@unittest.skipIf(test_hashlib.builtin_hashlib is None, 'test requires builtin_hashlib')
def test_pbkdf2_hmac_py():
    KDFTests._test_pbkdf2_hmac(test_hashlib.builtin_hashlib.pbkdf2_hmac, test_hashlib.builtin_hashes)

KDFTests = test_hashlib.KDFTests()
test_pbkdf2_hmac_py()
