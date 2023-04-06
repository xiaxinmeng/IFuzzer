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

def test_encoding_error_handler():
    with OpenTest.open(OpenTest.filename, 'wb') as f:
        f.write(b'foo\xffbar')
    with OpenTest.open(OpenTest.filename, 'rt', encoding='ascii', errors='ignore') as f:
        OpenTest.assertEqual(f.read(), 'foobar')

OpenTest = test_bz2.OpenTest()
test_encoding_error_handler()
