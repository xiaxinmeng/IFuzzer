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

def test_case_sha384_3():
    HashLibTestCase.check('sha384', b'a' * 1000000, '9d0e1809716474cb086e834e310a4a1ced149e9c00f248527972cec5704c2a5b' + '07b8b3dc38ecc4ebae97ddd87f3d8985')

HashLibTestCase = test_hashlib.HashLibTestCase()
test_case_sha384_3()
