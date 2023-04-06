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

def test_case_sha1_3():
    HashLibTestCase.check('sha1', b'a' * 1000000, '34aa973cd4c4daa4f61eeb2bdbad27316534016f')

HashLibTestCase = test_hashlib.HashLibTestCase()
test_case_sha1_3()
