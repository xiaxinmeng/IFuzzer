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
def test_realcopy():
    h1 = hmac.HMAC(b'key', digestmod='sha256')
    h2 = h1.copy()
    CopyTestCase.assertTrue(id(h1) != id(h2), 'No real copy of the HMAC instance.')
    CopyTestCase.assertTrue(id(h1._inner) != id(h2._inner), "No real copy of the attribute 'inner'.")
    CopyTestCase.assertTrue(id(h1._outer) != id(h2._outer), "No real copy of the attribute 'outer'.")
    CopyTestCase.assertEqual(h1._inner, h1.inner)
    CopyTestCase.assertEqual(h1._outer, h1.outer)
    CopyTestCase.assertEqual(h1._digest_cons, h1.digest_cons)

CopyTestCase = test_hmac.CopyTestCase()
test_realcopy()
