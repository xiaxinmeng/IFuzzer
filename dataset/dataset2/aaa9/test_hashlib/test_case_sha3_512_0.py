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

@test_hashlib.requires_sha3
def test_case_sha3_512_0():
    HashLibTestCase.check('sha3_512', b'', 'a69f73cca23a9ac5c8b567dc185a756e97c982164fe25859e0d1dcc1475c80a6' + '15b2123af1f5f94c11e3e9402c3ac558f500199d95b6d3e301758586281dcd26')

HashLibTestCase = test_hashlib.HashLibTestCase()
test_case_sha3_512_0()
