import unittest
from test import support
from test.support import import_helper
import binascii
import copy
import pickle
import random
import sys
from test.support import bigmemtest, _1G, _4G
import random
import test_zlib

def test_decompincflush():
    CompressObjectTestCase.test_decompinc(flush=True)

CompressObjectTestCase = test_zlib.CompressObjectTestCase()
test_decompincflush()
