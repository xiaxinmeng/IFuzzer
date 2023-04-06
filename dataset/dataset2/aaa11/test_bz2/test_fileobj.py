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

def test_fileobj():
    with OpenTest.open(BytesIO(OpenTest.DATA), 'r') as f:
        OpenTest.assertEqual(f.read(), OpenTest.TEXT)
    with OpenTest.open(BytesIO(OpenTest.DATA), 'rb') as f:
        OpenTest.assertEqual(f.read(), OpenTest.TEXT)
    text = OpenTest.TEXT.decode('ascii')
    with OpenTest.open(BytesIO(OpenTest.DATA), 'rt') as f:
        OpenTest.assertEqual(f.read(), text)

OpenTest = test_bz2.OpenTest()
test_fileobj()
