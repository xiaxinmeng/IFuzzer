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

def test_usedforsecurity_false():
    hashlib.new('sha256', usedforsecurity=False)
    for cons in HashLibTestCase.hash_constructors:
        cons(usedforsecurity=False)
        cons(b'', usedforsecurity=False)
    hashlib.new('md5', usedforsecurity=False)
    hashlib.md5(usedforsecurity=False)
    if HashLibTestCase._hashlib is not None:
        HashLibTestCase._hashlib.new('md5', usedforsecurity=False)
        HashLibTestCase._hashlib.openssl_md5(usedforsecurity=False)

HashLibTestCase = test_hashlib.HashLibTestCase()
test_usedforsecurity_false()
