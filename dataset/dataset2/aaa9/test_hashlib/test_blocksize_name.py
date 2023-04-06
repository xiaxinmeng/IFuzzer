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
from _hashlib import HASH, openssl_md_meth_names
import _blake2
import _sha3
import _md5
import test_hashlib

def test_blocksize_name():
    HashLibTestCase.check_blocksize_name('md5', 64, 16)
    HashLibTestCase.check_blocksize_name('sha1', 64, 20)
    HashLibTestCase.check_blocksize_name('sha224', 64, 28)
    HashLibTestCase.check_blocksize_name('sha256', 64, 32)
    HashLibTestCase.check_blocksize_name('sha384', 128, 48)
    HashLibTestCase.check_blocksize_name('sha512', 128, 64)

HashLibTestCase = test_hashlib.HashLibTestCase()
test_blocksize_name()
