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

@unittest.skipIf(sys.maxsize < _4G - 1, 'test cannot run on 32-bit systems')
@bigmemtest(size=_4G - 1, memuse=1, dry_run=False)
def test_case_md5_uintmax(HashLibTestCase, size):
    HashLibTestCase.check('md5', b'A' * size, '28138d306ff1b8281f1a9067e1a1a2b3')

HashLibTestCase = test_hashlib.HashLibTestCase()
test_case_md5_uintmax()
