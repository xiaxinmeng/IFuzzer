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

def test_case_sha512_3():
    HashLibTestCase.check('sha512', b'a' * 1000000, 'e718483d0ce769644e2e42c7bc15b4638e1f98b13b2044285632a803afa973eb' + 'de0ff244877ea60a4cb0432ce577c31beb009c5c2c49aa2e4eadb217ad8cc09b')

HashLibTestCase = test_hashlib.HashLibTestCase()
test_case_sha512_3()
