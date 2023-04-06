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

@test_hashlib.requires_sha3
def test_extra_sha3():
    HashLibTestCase.check_sha3('sha3_224', 448, 1152, b'\x06')
    HashLibTestCase.check_sha3('sha3_256', 512, 1088, b'\x06')
    HashLibTestCase.check_sha3('sha3_384', 768, 832, b'\x06')
    HashLibTestCase.check_sha3('sha3_512', 1024, 576, b'\x06')
    HashLibTestCase.check_sha3('shake_128', 256, 1344, b'\x1f')
    HashLibTestCase.check_sha3('shake_256', 512, 1088, b'\x1f')

HashLibTestCase = test_hashlib.HashLibTestCase()
test_extra_sha3()
