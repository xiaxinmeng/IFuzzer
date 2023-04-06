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

def test_case_sha224_3():
    HashLibTestCase.check('sha224', b'a' * 1000000, '20794655980c91d8bbb4c1ea97618a4bf03f42581948b2ee4ee7ad67')

HashLibTestCase = test_hashlib.HashLibTestCase()
test_case_sha224_3()
