import binascii
import functools
import hmac
import hashlib
import unittest
import unittest.mock
import warnings
from test.support import hashlib_helper
from _operator import _compare_digest as operator_compare_digest
from _hashlib import HMAC as C_HMAC
from _hashlib import hmac_new as c_hmac_new
from _hashlib import compare_digest as openssl_compare_digest
import test_hmac

@unittest.skipUnless(C_HMAC is not None, 'need _hashlib')
def test_internal_types():
    with ConstructorTestCase.assertRaisesRegex(TypeError, "cannot create 'HMAC' instance"):
        C_HMAC()

ConstructorTestCase = test_hmac.ConstructorTestCase()
test_internal_types()
