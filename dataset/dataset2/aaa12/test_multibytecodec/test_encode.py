from test import support
from test.support import os_helper
from test.support.os_helper import TESTFN
import unittest, io, codecs, sys
import _multibytecodec
import test_multibytecodec

def test_encode():
    TestStateful.assertEqual(TestStateful.text.encode(TestStateful.encoding), TestStateful.expected_reset)

TestStateful = test_multibytecodec.TestStateful()
test_encode()
