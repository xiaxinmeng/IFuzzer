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
def test_blake2b():
    HashLibTestCase.check_blake2(hashlib.blake2b, 16, 16, 64, 64, (1 << 64) - 1)
    b2b_md_len = [20, 32, 48, 64]
    b2b_in_len = [0, 3, 128, 129, 255, 1024]
    HashLibTestCase.assertEqual(HashLibTestCase.blake2_rfc7693(hashlib.blake2b, b2b_md_len, b2b_in_len), 'c23a7800d98123bd10f506c61e29da5603d763b8bbad2e737f5e765a7bccd475')

HashLibTestCase = test_hashlib.HashLibTestCase()
test_blake2b()
