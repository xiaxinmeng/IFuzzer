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
def test_case_shake_256_0():
    HashLibTestCase.check('shake_256', b'', '46b9dd2b0ba88d13233b3feb743eeb243fcd52ea62b81b82b50c27646ed5762f', True)
    HashLibTestCase.check('shake_256', b'', '46b9', True)

HashLibTestCase = test_hashlib.HashLibTestCase()
test_case_shake_256_0()
