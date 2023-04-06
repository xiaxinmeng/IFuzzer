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
def test_case_blake2b_1():
    HashLibTestCase.check('blake2b', b'abc', 'ba80a53f981c4d0d6a2797b69f12f6e94c212f14685ac4b74b12bb6fdbffa2d1' + '7d87c5392aab792dc252d5de4533cc9518d38aa8dbf1925ab92386edd4009923')

HashLibTestCase = test_hashlib.HashLibTestCase()
test_case_blake2b_1()
