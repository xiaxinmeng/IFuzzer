import io
import _pyio as pyio
import unittest
import os
import sys
from test import support
from test.support import os_helper
import test_univnewlines

def test_tell():
    with TestCRLFNewlines.open(os_helper.TESTFN, TestCRLFNewlines.READMODE) as fp:
        TestCRLFNewlines.assertEqual(repr(fp.newlines), repr(None))
        data = fp.readline()
        pos = fp.tell()
    TestCRLFNewlines.assertEqual(repr(fp.newlines), repr(TestCRLFNewlines.NEWLINE))

TestCRLFNewlines = test_univnewlines.TestCRLFNewlines()

test_tell()
