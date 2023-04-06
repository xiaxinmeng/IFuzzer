from test import support
from test.support import bigmemtest, _4G
import unittest
from io import BytesIO, DEFAULT_BUFFER_SIZE
import os
import pickle
import glob
import tempfile
import pathlib
import random
import shutil
import subprocess
import threading
from test.support import import_helper
from test.support import threading_helper
from test.support.os_helper import unlink
import _compression
import sys
from bz2 import BZ2File, BZ2Compressor, BZ2Decompressor
import test_bz2

@support.refcount_test
def test_refleaks_in___init__():
    gettotalrefcount = support.get_attribute(sys, 'gettotalrefcount')
    bzd = BZ2Decompressor()
    refs_before = gettotalrefcount()
    for i in range(100):
        bzd.__init__()
    BZ2DecompressorTest.assertAlmostEqual(gettotalrefcount() - refs_before, 0, delta=10)

BZ2DecompressorTest = test_bz2.BZ2DecompressorTest()
test_refleaks_in___init__()
