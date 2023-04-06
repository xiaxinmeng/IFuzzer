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

def test_case_sha512_0():
    HashLibTestCase.check('sha512', b'', 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce' + '47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e')

HashLibTestCase = test_hashlib.HashLibTestCase()
test_case_sha512_0()
