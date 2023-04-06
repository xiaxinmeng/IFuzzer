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

def test_x_mode():
    for mode in ('x', 'xb', 'xt'):
        unlink(OpenTest.filename)
        with OpenTest.open(OpenTest.filename, mode) as f:
            pass
        with OpenTest.assertRaises(FileExistsError):
            with OpenTest.open(OpenTest.filename, mode) as f:
                pass

OpenTest = test_bz2.OpenTest()
test_x_mode()
