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

def test_decompressor_inputbuf_3():
    bzd = BZ2Decompressor()
    out = []
    out.append(bzd.decompress(BZ2DecompressorTest.DATA[:200], 5))
    out.append(bzd.decompress(BZ2DecompressorTest.DATA[200:300], 5))
    out.append(bzd.decompress(BZ2DecompressorTest.DATA[300:]))
    BZ2DecompressorTest.assertEqual(b''.join(out), BZ2DecompressorTest.TEXT)

BZ2DecompressorTest = test_bz2.BZ2DecompressorTest()
test_decompressor_inputbuf_3()
