from test.support import findfile
from test.support.os_helper import TESTFN, unlink
from test.support.warnings_helper import check_no_resource_warning
import unittest
from unittest import mock
from test import audiotests
from audioop import byteswap
import io
import sys
import struct
import aifc
import test_aifc

def test_skipunknown():
    f = aifc.open(findfile('Sine-1000Hz-300ms.aif'))
    f.close()

AifcMiscTest = test_aifc.AifcMiscTest()
test_skipunknown()
