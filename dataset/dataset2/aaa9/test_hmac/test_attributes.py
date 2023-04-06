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

@hashlib_helper.requires_hashdigest('sha256')
def test_attributes():
    h1 = hmac.HMAC(b'key', digestmod='sha256')
    h2 = h1.copy()
    CopyTestCase.assertTrue(h1._digest_cons == h2._digest_cons, "digest constructors don't match.")
    CopyTestCase.assertEqual(type(h1._inner), type(h2._inner), "Types of inner don't match.")
    CopyTestCase.assertEqual(type(h1._outer), type(h2._outer), "Types of outer don't match.")

CopyTestCase = test_hmac.CopyTestCase()
test_attributes()
