import importlib
import unittest
import os, sys
import os.path
from test import support

def test_importlib_cache():

    with support.temp_dir() as path:
        dirname, basename = os.path.split(path)
        os.mkdir(os.path.join(path, 'test2'))
        importlib.invalidate_caches()

        with support.DirsOnSysPath(dirname):
            __import__("{basename}.test2".format(basename=basename))


class Tests(unittest.TestCase):

    def test_bug(self):
        for _ in range(10):
            test_importlib_cache()