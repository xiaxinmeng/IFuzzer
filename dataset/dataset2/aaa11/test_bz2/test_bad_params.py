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

def test_bad_params():
    OpenTest.assertRaises(ValueError, OpenTest.open, OpenTest.filename, 'wbt')
    OpenTest.assertRaises(ValueError, OpenTest.open, OpenTest.filename, 'xbt')
    OpenTest.assertRaises(ValueError, OpenTest.open, OpenTest.filename, 'rb', encoding='utf-8')
    OpenTest.assertRaises(ValueError, OpenTest.open, OpenTest.filename, 'rb', errors='ignore')
    OpenTest.assertRaises(ValueError, OpenTest.open, OpenTest.filename, 'rb', newline='\n')

OpenTest = test_bz2.OpenTest()
test_bad_params()
