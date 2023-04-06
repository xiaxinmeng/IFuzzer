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
def test_exercise_all_methods():
    try:
        h = hmac.HMAC(b'my secret key', digestmod='sha256')
        h.update(b'compute the hash of this text!')
        h.digest()
        h.hexdigest()
        h.copy()
    except Exception:
        SanityTestCase.fail('Exception raised during normal usage of HMAC class.')

SanityTestCase = test_hmac.SanityTestCase()
test_exercise_all_methods()
