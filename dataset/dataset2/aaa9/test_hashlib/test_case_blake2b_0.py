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
def test_case_blake2b_0():
    HashLibTestCase.check('blake2b', b'', '786a02f742015903c6c6fd852552d272912f4740e15847618a86e217f71f5419' + 'd25e1031afee585313896444934eb04b903a685b1448b755d56f701afe9be2ce')

HashLibTestCase = test_hashlib.HashLibTestCase()
test_case_blake2b_0()
