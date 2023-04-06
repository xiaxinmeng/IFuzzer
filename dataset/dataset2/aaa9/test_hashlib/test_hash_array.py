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

def test_hash_array():
    a = array.array('b', range(10))
    for cons in HashLibTestCase.hash_constructors:
        c = cons(a, usedforsecurity=False)
        if c.name in HashLibTestCase.shakes:
            c.hexdigest(16)
        else:
            c.hexdigest()

HashLibTestCase = test_hashlib.HashLibTestCase()
test_hash_array()
