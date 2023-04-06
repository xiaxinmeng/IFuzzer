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
def test_case_shake128_vector():
    for (msg, md) in test_hashlib.read_vectors('shake_128'):
        HashLibTestCase.check('shake_128', msg, md, True)

HashLibTestCase = test_hashlib.HashLibTestCase()
test_case_shake128_vector()
