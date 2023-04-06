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
def test_blake2s():
    HashLibTestCase.check_blake2(hashlib.blake2s, 8, 8, 32, 32, (1 << 48) - 1)
    b2s_md_len = [16, 20, 28, 32]
    b2s_in_len = [0, 3, 64, 65, 255, 1024]
    HashLibTestCase.assertEqual(HashLibTestCase.blake2_rfc7693(hashlib.blake2s, b2s_md_len, b2s_in_len), '6a411f08ce25adcdfb02aba641451cec53c598b24f4fc787fbdc88797f4c1dfe')

HashLibTestCase = test_hashlib.HashLibTestCase()
test_blake2s()
