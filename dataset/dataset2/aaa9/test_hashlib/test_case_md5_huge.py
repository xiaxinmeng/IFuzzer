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

@unittest.skipIf(sys.maxsize < _4G + 5, 'test cannot run on 32-bit systems')
@bigmemtest(size=_4G + 5, memuse=1, dry_run=False)
def test_case_md5_huge(HashLibTestCase, size):
    HashLibTestCase.check('md5', b'A' * size, 'c9af2dff37468ce5dfee8f2cfc0a9c6d')

HashLibTestCase = test_hashlib.HashLibTestCase()
test_case_md5_huge()
