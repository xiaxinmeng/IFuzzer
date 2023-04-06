import io
import _pyio as pyio
import unittest
import os
import sys
from test import support
from test.support import os_helper
import test_univnewlines

def test_readlines():
    with TestGenericUnivNewlines.open(os_helper.TESTFN, TestGenericUnivNewlines.READMODE) as fp:
        data = fp.readlines()
    TestGenericUnivNewlines.assertEqual(data, DATA_SPLIT)
    TestGenericUnivNewlines.assertEqual(repr(fp.newlines), repr(TestGenericUnivNewlines.NEWLINE))

TestGenericUnivNewlines = test_univnewlines.TestGenericUnivNewlines()
TestGenericUnivNewlines.setUp()
test_readlines()
