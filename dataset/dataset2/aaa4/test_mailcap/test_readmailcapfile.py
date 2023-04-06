import mailcap
import os
import copy
import test.support
from test.support import os_helper
import unittest
import sys
import test_mailcap

def test_readmailcapfile():
    with open(test_mailcap.MAILCAPFILE, 'r') as mcf:
        with HelperFunctionTest.assertWarns(DeprecationWarning):
            d = mailcap.readmailcapfile(mcf)
    HelperFunctionTest.assertDictEqual(d, test_mailcap.MAILCAPDICT_DEPRECATED)

HelperFunctionTest = test_mailcap.HelperFunctionTest()
test_readmailcapfile()
